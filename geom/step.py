"""
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
"""

"""
OpenSim Gait2392 bodies customisation
"""

import os
import json

from geom import gait2392geomcustomiser

SELF_DIR = os.path.split(os.path.realpath(__file__))[0]
TEMPLATE_OSIM_FILENAME = os.path.join(SELF_DIR, 'data\gait2392_simbody.osim')

class FieldworkGait2392GeomStep:
    '''
    Step for customising the OpenSim Gait2392 model geometry using
    fieldwork models. Parameters modified are body frame definitions, visual
    meshes, and the scaling of non-patient-specific bodies. Gait2392
    parameters are customised based on the inputs. If both inputs are
    provided, the bone meshes in the lowerlimbatlas will be updated
    with the meshes in the fieldworkmodeldict.

    Inputs
    ------
    gias-lowerlimb : gias2.musculoskeletal.bonemodel.LowerLimbAtlas instance
        Lower limb model to be used to customise gait2392.
    fieldworkmodeldict : dict [optional]
        Bone models to be used to customisation gait2392.
        Dictionary keys should be:
            pelvis
            femur-l
            femur-r
            patella-l
            patella-r
            tibiafibula-l
            tibiafibula-r
    
    Outputs
    -------
    opensimmodel : opensim.model instance
        The customised gait2392 opensim model
    gias-lowerlimb : gias2.musculoskeletal.bonemodel.LowerLimbAtlas instance
        The lowerlimb model used in the customisation
    '''

    def __init__(self, config):

        self._config = {}
        self._config = config
        self._g2392Cust = gait2392geomcustomiser.Gait2392GeomCustomiser(self._config)
        self.inputModels = None
        self.inputLLAtlas = None

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        self._g2392Cust.init_osim_model()
        if self.inputLLAtlas is not None:
            self._g2392Cust.set_lowerlimb_atlas(self.inputLLAtlas)
        if self.inputModels is not None:
            self._g2392Cust.set_lowerlimb_gfields(self.inputModels)
        self._g2392Cust.customise()

    def getInput(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self.inputLLAtlas = dataIn # gias-lowerlimb
        elif index == 1:
            self._g2392Cust.input_markers = dataIn
        else:
            self.inputModels = dataIn # ju#fieldworkmodeldict

    def output(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        if index==3:
            return self._g2392Cust.osimmodel._model
        else:
            return self._g2392Cust.LL

    

  

