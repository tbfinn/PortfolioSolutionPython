#   File: Controller.py
#  
#   Author:  Timothy B. Finn (tbf.lodi@gmail.com)
#   Date:     Spring 2021
#   Project:   Portfolio Project
#  
#   Summary of File:
#
#
#
#
import Model
import ViewModel
import PlanManager
import RobotManager
import DetectorManager
import RunManager
import DBManager

class Controller(object):
    """description of class"""


    # inject model
    def __init__(self, model, planmanager, robotmanager, detectormanager, runmanager, dbmanager):
        self.model = Model
        self.planmanager = PlanManager 
        self.robotmanager = RobotManager
        self.detectormanager = DetectorManager
        self.runmanager = RunManager
        self.dbmanager = DBManager