#   File: PortfolioPython.py
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
import Controller
import Model
import ViewModel
import PlanManager
import RobotManager
import DetectorManager
import RunManager
import DBManager

def main():
   
    # inject MVC components
    viewModel = ViewModel()
    model = Model(viewModel)
    controller = Controller(model, planmanager, robotmanager, detectormanager, runmanager, dbmanager)





if __name__ == '__main__':
    main()
