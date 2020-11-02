
'''
MAP Client Plugin Step
'''
import os
import json

from fieldwork import llstep

DEFAULT_MODEL_LANDMARKS = (
    'pelvis-LASIS', 'pelvis-RASIS', 'pelvis-Sacral',
    'femur-MEC-l', 'femur-LEC-l', 
    'femur-MEC-r', 'femur-LEC-r',
    'tibiafibula-MM-l', 'tibiafibula-LM-l',
    'tibiafibula-MM-r', 'tibiafibula-LM-r',
    )

class FieldworkLowerLimb2SideGenerationStep:
    '''
    Step for customising the lower limb bones to motion capture markers.

    Inputs
    ------
    landmarks : dict
        Dictionary of marker names : marker coordinates

    Outputs
    -------
    fieldworkmodeldict : dict
        A dictionary of customised fieldwork models of lower limb bones.
        Dictionary keys are: "pelvis", "pelvis flat", 'hemipelvis-left",
        "hemipelvis-right", "sacrum", "femur-l", "femur-r", "tibiafibula-l",
        "tibiafibula-r", "tibia-l", "tibia-r", "fibula-l", 'fibula-r",
        "patella-l", "patella-r".
    LowerLimbAtlas : LowerLimbAtlas instance
    '''

    def __init__(self, config):

        self._config = {}
        self._config = config
        self._data = llstep.LLStepData(self._config)

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        self._data.loadData()
        self._data.updateFromConfig()
        print('LL estimation configs:')
        print(self._data.config)
        self._data.register()

    def output(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index == 1:
            print('outputting {}'.format(self._data.outputModelDict.keys()))
            return self._data.outputModelDict
        else:
            return self._data.LL

   


