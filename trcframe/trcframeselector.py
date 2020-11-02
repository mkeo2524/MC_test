import numpy as np

def trcframeselect(trcdata, frame):
    landmarksNames = trcdata['Labels']
    try:
            time, landmarksCoords = trcdata[frame]
    except KeyError:
            print('Frame {} not found'.format(frame))
            raise KeyError
    landmarksNamesData = [frame, time] + landmarksCoords
    landmarks = dict(zip(landmarksNames, landmarksNamesData))
    if 'Frame#' in landmarks:
            del landmarks['Frame#']
    if 'Time' in landmarks:
        del landmarks['Time']

    for k, v in landmarks.items():
        landmarks[k] = np.array(v)
    return landmarks



    
    