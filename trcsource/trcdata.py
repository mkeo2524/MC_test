
def load(filename):
    trcdata = {}
    header_read_successfully = False
    labels = []
    with open(filename) as f:
        contents = f.readlines()
        line_count = 0
        for line in contents:
            line_count += 1
            line = line.strip()
            if line_count == 1:
                # File Header 1
                sections = line.split('\t')
                trcdata[sections[0]] = sections[1]
                trcdata['DataFormat'] = sections[2]
                data_format_count = len(sections[2].split('/'))
                trcdata['FileName'] = sections[3]
            elif line_count == 2:
                # File Header 2
                file_header_keys = line.split('\t')
            elif line_count == 3:
                # File Header 3
                file_header_data = line.split('\t')
                if len(file_header_keys) == len(file_header_data):
                    for index, key in enumerate(file_header_keys):
                        if key == 'Units':
                            trcdata[key] = file_header_data[index]
                        else:
                            trcdata[key] = float(file_header_data[index])
                else:
                    raise IOError('File format invalid: File header keys count (%d) is not equal to file header data count (%d)' % (len(file_header_keys), len(file_header_data)))
            elif line_count == 4:
                # Data Header 1
                data_header_labels = line.split('\t')
                if data_header_labels[0] != 'Frame#':
                    raise IOError('File format not valid data header does not start with "Frame#".')
                if data_header_labels[1] != 'Time':
                    raise IOError('File format not valid data header in position 2 is not "Time".')

                trcdata['Frame#'] = []
                trcdata['Time'] = []
            elif line_count == 5:
                # Data Header 1
                data_header_sublabels = line.split('\t')
                if len(data_header_labels) != len(data_header_sublabels):
                    raise IOError('File format invalid: Data header labels count (%d) is not equal to data header sub-labels count (%d)' % (len(data_header_labels), len(data_header_sublabels)))

                labels = []
                for label in data_header_labels:
                    label = label.strip()
                    if len(label):
                        trcdata[label] = []
                        labels.append(label)

                trcdata['Labels'] = labels
            elif line_count == 6 and len(line) == 0:
                # Blank line
                header_read_successfully = True
            else:
                # Some files don't have a blank line at line six
                if line_count == 6:
                    header_read_successfully = True
                # Data section
                if header_read_successfully:
                    sections = line.split('\t')

                    frame = int(sections.pop(0))
                    trcdata['Frame#'].append(frame)

                    time = float(sections.pop(0))
                    trcdata['Time'].append(time)

                    len_section = len(sections)
                    if len_section % data_format_count == 0:
                        data = [[float(sections[subindex]) for subindex in range(index, index + data_format_count)] for index in range(0, len_section, data_format_count)]
                        trcdata[frame] = (time, data)

                        for index, label_data in enumerate(data):
                            # Add two to the index as we want to skip 'Frame#' and 'Time'
                            trcdata[labels[index + 2]] += [label_data]

                    else:
                        raise IOError('File format invalid: data frame %d does not match the data format' % len_section)
    return trcdata

