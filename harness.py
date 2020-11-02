import os
from trcsource.trcdata import load
from trcframe.trcframeselector import trcframeselect
from zipoutput import output_zip
from model import run

# path to trc file
#path = os.environ('TRC_FILE') \
##    if os.environ('TRC_FILE') else r'C:\Users\mkeo2\Desktop\MC\server\trcs\StaticCalibration.trc'
#osim_out_dir = os.environ('OSIM_OUTPUT_DIR') \
#    if os.environ('OSIM_OUTPUT_DIR') else r'C:\Users\mkeo2\Desktop\MC\server\backend\geom\osim'

path = r'C:\Users\mkeo2\Desktop\MC\server\trcs\StaticCalibration.trc' #insert trc path here
osim_out_dir = r'C:\Users\mkeo2\Desktop\MC\server\backend\geom\osim' #insert .osim output directory
trcData = load(path)  # load trc data
trcFrame = trcframeselect(trcData, 100)  # get marker coordinates for all frames

# choose your anatomical landmarks pairs
landmarks = {
    'femur-HC-l': 'LHJC',
    'femur-HC-r': 'RHJC',
    'femur-LEC-l': 'LLFC',
    'femur-LEC-r': 'RLFC',
    'femur-MEC-l': 'LMFC',
    'femur-MEC-r': 'RMFC',
    'pelvis-LASIS': 'LASI',
    'pelvis-LPSIS': 'LPSI',
    'pelvis-RASIS': 'RASI',
    'pelvis-RPSIS': 'RPSI',
    'tibiafibula-LM-l': 'LLMAL',
    'tibiafibula-LM-r': 'RLMAL',
    'tibiafibula-MM-l': 'LMMAL',
    'tibiafibula-MM-r': 'RMMAL'
}
# choose your tracking marker pairs
'''
Possible target marker pairs are:
adj_marker_pairs = {
    'L.ASIS: ',
    'L.Acromium: ',
    'L.Ankle.Lat: ',
    'L.Ankle.Med: ',
    'L.FHC: ',
    'L.HJC: ',
    'L.Heel: ',
    'L.Knee.Lat: ',
    'L.Knee.Med: ',
    'L.Midfoot.Lat: ',
    'L.Midfoot.Sup: ',
    'L.Shank.Front: ',
    'L.Shank.Upper: ',
    'L.Thigh.Front: ',
    'L.Thigh.Rear: ',
    'L.Thigh.Upper: ',
    'L.Tib.KJC: ',
    'L.Toe.Lat: ',
    'L.Toe.Med: ',
    'L.Toe.Tip: ',
    'R.ASIS: ',
    'R.Acromium: ',
    'R.Ankle.Lat: ',
    'R.Ankle.Med: ',
    'R.FHC: ',
    'R.HJC: ',
    'R.Heel: ',
    'R.Knee.Lat: ',
    'R.Knee.Med: ',
    'R.Midfoot.Lat: ',
    'R.Midfoot.Sup: ',
    'R.Shank.Front: ',
    'R.Shank.Upper: ',
    'R.Thigh.Front: ',
    'R.Thigh.Rear: ',
    'R.Thigh.Upper: ',
    'R.Tib.KJC: ',
    'R.Toe.Lat: ',
    'R.Toe.Med: ',
    'R.Toe.Tip: ',
    'Sternum: ',
    'Top.Head: ',
    'V.Sacral: '
}
'''

adj_marker_pairs = {
    '''
    Insert actual pairs here
    '''
}
# inputs for fieldwork step
generation_config = {'identifier': '', 'GUI': False, 'registration_mode': 'shapemodel', 'pcs_to_fit': '1',
                     'mweight': '0.1',
                     'knee_corr': False, 'knee_dof': True, 'marker_radius': '5.0', 'skin_pad': '5.0',
                     'landmarks': landmarks}

#inputs for geometry step
geometry_config = {'identifier': '', 'GUI': False, 'scale_other_bodies': True, 'in_unit': 'mm', 'out_unit': 'm',
                   'osim_output_dir': osim_out_dir,
                   'write_osim_file': True, 'subject_mass': None, 'preserve_mass_distribution': False,
                   'adj_marker_pairs': adj_marker_pairs}

#inputs for musclesomso step
muscle_config = {'osim_output_dir': osim_out_dir, 'in_unit': 'cm',
                 'out_unit': 'm', 'write_osim_file': True, 'update_knee_splines': False, 'static_vas': False,
                 'update_max_iso_forces': True, 'subject_height': '169', 'subject_mass': '56'}


if __name__ == "__main__":
    run(trcFrame, generation_config, geometry_config, muscle_config)
    output_zip()

