
'''
MAP Client Plugin Step
'''
import json




from muscle import gait2392musclecustsomso


class FieldworkGait2392SomsoMuscleStep:
    '''
    MAP Client plugin for customising the OpenSim Gait2392 model muscle points

    Inputs
    ------
    gias-lowerlimb : GIAS2 LowerlimbAtlas instance
        Lower limb model with customised lower limb bone geometry and pose
    osimmodel : OpenSim model instance
        The opensim model to modify. Should be output from a step that
        modified the body geometries.

    Outputs
    -------
    osimmodel : OpenSim model instance
        Modified opensim model
    '''

    def __init__(self, config):
        

        # Config:
        self._config = {}
        self._config = config
        self._g2392_somso_muscle = gait2392musclecustsomso.gait2392MuscleCustomiser(self._config)

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        self._g2392_somso_muscle.config = self._config
        self._g2392_somso_muscle.customise()
        

    def inputData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self._g2392_somso_muscle.ll = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#gias-lowerlimb
        elif index == 1:
            self._g2392_somso_muscle.set_osim_model(dataIn) # http://physiomeproject.org/workflow/1.0/rdf-schema#osimmodel
        elif index == 2:
			self._g2392_somso_muscle.landmarks = dataIn
    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self._g2392_somso_muscle.gias_osimmodel._model # http://physiomeproject.org/workflow/1.0/rdf-schema#osimmodel

    