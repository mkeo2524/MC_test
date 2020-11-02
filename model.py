import os
import json

from trcsource.trcdata import load
from trcframe.trcframeselector import trcframeselect
from fieldwork.step import FieldworkLowerLimb2SideGenerationStep
from geom.step import FieldworkGait2392GeomStep
from muscle.step import FieldworkGait2392SomsoMuscleStep

DEFAULT_MODEL_LANDMARKS = (
    'pelvis-LASIS', 'pelvis-RASIS', 'pelvis-Sacral',
    'femur-MEC-l', 'femur-LEC-l',
    'femur-MEC-r', 'femur-LEC-r',
    'tibiafibula-MM-l', 'tibiafibula-LM-l',
    'tibiafibula-MM-r', 'tibiafibula-LM-r',
)


def run(trc_frame, generation_config, geometry_config, muscle_config):
    fieldworkModel = FieldworkLowerLimb2SideGenerationStep(generation_config)  # initialise fieldwork class
    fieldworkModel._data.inputLandmarks = trc_frame  # input landmark frames
    fieldworkModel.execute()  # execute plugin
    lowerLimb = fieldworkModel.output(2)  # gias2 lower limb
    fwLandmarks = fieldworkModel.output(1)  # fieldwork anatomical landmarks

    geomModel = FieldworkGait2392GeomStep(geometry_config)  # initialise geom class
    geomModel.getInput(0, lowerLimb)  # input gias2 lower limb
    geomModel.getInput(1, 'input tracking markers')
    geomModel.getInput(-1, fwLandmarks)  # input gias2 landmarks
    geomModel.execute()  # execute plugin

    geomLowerLimb = geomModel.output(-1)
    osimModel = geomModel.output(3)

    muscleModel = FieldworkGait2392SomsoMuscleStep(muscle_config)
    muscleModel.inputData(0, geomLowerLimb)
    muscleModel.inputData(1, osimModel)
    muscleModel.inputData(2, fwLandmarks)
    muscleModel.execute()
