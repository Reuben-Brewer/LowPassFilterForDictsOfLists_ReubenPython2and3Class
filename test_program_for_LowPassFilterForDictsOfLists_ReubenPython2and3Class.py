# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision D, 07/31/2024

Verified working on: Python 3.8 for Windows 10 64-bit, Ubuntu 20.04, and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

###########################################################
from LowPassFilterForDictsOfLists_ReubenPython2and3Class import *
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import math, numpy
import traceback
import re
import random
from random import randint
###########################################################

###########################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
###########################################################

###########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
###########################################################

#######################################################################################################################
#######################################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def UpdateFrequencyCalculation():
    global CurrentTime_MainLoopThread
    global LastTime_MainLoopThread
    global DataStreamingFrequency_MainLoopThread
    global DataStreamingDeltaT_MainLoopThread
    global Counter_MainLoopThread

    try:
        DataStreamingDeltaT_MainLoopThread = CurrentTime_MainLoopThread - LastTime_MainLoopThread

        if DataStreamingDeltaT_MainLoopThread != 0.0:
            DataStreamingFrequency_MainLoopThread = 1.0 / DataStreamingDeltaT_MainLoopThread

        LastTime_MainLoopThread = CurrentTime_MainLoopThread
        Counter_MainLoopThread = Counter_MainLoopThread + 1

    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation ERROR, Exceptions: %s" % exceptions)
        traceback.print_exc()
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
if __name__ == '__main__':

    ####################################################
    ####################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global USE_LOWPASSFILTER_FLAG
    USE_LOWPASSFILTER_FLAG = 1

    global USE_PLOTTER_FLAG
    USE_PLOTTER_FLAG = 1

    global USE_SPECKLE_NOISE_FLAG
    USE_SPECKLE_NOISE_FLAG = 1
    ####################################################
    ####################################################
    
    ####################################################
    ####################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global LastTime_MainLoopThread
    LastTime_MainLoopThread = -11111.0

    global DataStreamingFrequency_MainLoopThread
    DataStreamingFrequency_MainLoopThread = -11111.0

    global DataStreamingDeltaT_MainLoopThread
    DataStreamingDeltaT_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -1

    global Counter_MainLoopThread
    Counter_MainLoopThread = 0

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 1.0

    global SINUSOIDAL_MOTION_INPUT_MinValue
    SINUSOIDAL_MOTION_INPUT_MinValue = -90.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue
    SINUSOIDAL_MOTION_INPUT_MaxValue = 90.0

    global NoiseCounter
    NoiseCounter = 0

    global NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude
    NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude = 0.1
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject

    global LOWPASSFILTER_OPEN_FLAG
    LOWPASSFILTER_OPEN_FLAG = -1

    global LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict
    LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict = dict()

    global Raw_1
    Raw_1 = 0.0
    
    global Filtered_1
    Filtered_1 = 0.0

    global Raw_2
    Raw_2 = 0.0

    global Filtered_2
    Filtered_2 = 0.0
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global PLOTTER_OPEN_FLAG
    PLOTTER_OPEN_FLAG = -1
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    if USE_LOWPASSFILTER_FLAG == 1:
        try:

            DictOfVariableFilterSettings = dict([("desired_angle_deg_1", dict([("UseMedianFilterFlag", 1), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", 0.20)])), #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value
                                                    ("desired_angle_deg_2", dict([("UseMedianFilterFlag", 0), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", 0.6)]))])

            #LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_setup_dict = dict([("DictOfVariableFilterSettings", DictOfVariableFilterSettings)])
            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_setup_dict = dict()

            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject = LowPassFilterForDictsOfLists_ReubenPython2and3Class(LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_setup_dict)
            LOWPASSFILTER_OPEN_FLAG = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDictOfVariableFilterSettingsFromExternalProgram(DictOfVariableFilterSettings)

        except:
            exceptions = sys.exc_info()[0]
            print("LowPassFilterForDictsOfLists_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
    ####################################################
    ####################################################

    #################################################
    #################################################
    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1



    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("GraphCanvasWidth", 1280),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 1.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["Raw_1", "Filtered_1", "Raw_2", "Filtered_2"]),("ColorList", ["Red", "Green", "Orange", "Blue"])])),
                                                                                        ("NumberOfDataPointToPlot", 50),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 0),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 20.0),
                                                                                        ("Y_min", 1.1*SINUSOIDAL_MOTION_INPUT_MinValue),
                                                                                        ("Y_max", 1.1*SINUSOIDAL_MOTION_INPUT_MaxValue),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])

    if USE_PLOTTER_FLAG == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            PLOTTER_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    ####################################################
    ####################################################
    if LOWPASSFILTER_OPEN_FLAG != 1:
        print("Failed to open LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    ####################################################
    ####################################################

    #################################################
    #################################################
    if USE_PLOTTER_FLAG == 1 and PLOTTER_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterClass_Object.")
        ExitProgram_Callback()
    #################################################
    #################################################

    ####################################################
    ####################################################
    random.seed()
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    ####################################################

    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()
    while(EXIT_PROGRAM_FLAG == 0 and CurrentTime_MainLoopThread <= 10.0):
        ####################################################
        ####################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ####################################################
        ####################################################

        #################################################### GET's
        ####################################################
        if LOWPASSFILTER_OPEN_FLAG == 1:

            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.GetMostRecentDataDict()
            #print("LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict: " + str(LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict))

            if "TestList" in LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict or "desired_angle_deg_1" in LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict:

                #'''
                Raw_1 = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["desired_angle_deg_1"]["Raw_MostRecentValuesList"]
                Filtered_1 = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["desired_angle_deg_1"]["Filtered_MostRecentValuesList"]

                Raw_2 = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["desired_angle_deg_2"]["Raw_MostRecentValuesList"]
                Filtered_2 = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["desired_angle_deg_2"]["Filtered_MostRecentValuesList"]
                #'''

                #[Raw_1, Raw_2] = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["TestList"]["Raw_MostRecentValuesList"]
                #[Filtered_1, Filtered_2] = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["TestList"]["Filtered_MostRecentValuesList"]

        ####################################################
        ####################################################

        #################################################### SET's
        ####################################################
        if LOWPASSFILTER_OPEN_FLAG == 1:
            time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
            desired_angle_deg_1 = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + 0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.sin(time_gain * CurrentTime_MainLoopThread)  #math.exp(0.1*CurrentTime_MainLoopThread)*0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) *
            desired_angle_deg_2 = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + 0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.cos(time_gain * CurrentTime_MainLoopThread)


            ####################################################
            if USE_SPECKLE_NOISE_FLAG == 1:
                NoiseCounter = NoiseCounter + 1
                if NoiseCounter == 1:
                    NoiseAmplitude = NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)
                    
                    NoiseValue_1 = random.uniform(-1.0*NoiseAmplitude, NoiseAmplitude)
                    desired_angle_deg_1 = desired_angle_deg_1 + NoiseValue_1
                    
                    NoiseValue_2 = random.uniform(-1.0*NoiseAmplitude, NoiseAmplitude)
                    desired_angle_deg_2 = desired_angle_deg_2 + NoiseValue_2
                    
                    NoiseCounter = 0
            ####################################################

            #'''
            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDataDictFromExternalProgram(dict([("desired_angle_deg_1", [desired_angle_deg_1, desired_angle_deg_1]),
                                                                                                    ("desired_angle_deg_2", [desired_angle_deg_2, desired_angle_deg_2])]))
            #'''

            #LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDataDictFromExternalProgram(dict([("TestList", [desired_angle_deg_1, desired_angle_deg_2])]))
        ####################################################
        ####################################################

        ####################################################
        ####################################################
        if PLOTTER_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]
            else:
                pass
            ####################################################

            ####################################################
            if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                dummy = 0

                #'''
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Raw_1", "Filtered_1", "Raw_2", "Filtered_2"],
                                                                                                                        [CurrentTime_MainLoopThread]*4,
                                                                                                                        [Raw_1[0], Filtered_1[0], Raw_2[0], Filtered_2[0]])
                #'''

                '''
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Raw_1", "Filtered_1"],
                                                                                                                        [CurrentTime_MainLoopThread]*2,
                                                                                                                        [Raw_1, Filtered_1])
                '''
            ####################################################

        ####################################################
        ####################################################

        ####################################################
        ####################################################
        UpdateFrequencyCalculation()
        #print(DataStreamingFrequency_MainLoopThread)
        time.sleep(0.040)
        #time.sleep(0.001)
        ####################################################
        ####################################################

    ####################################################
    ####################################################
    ####################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class.")

    #################################################
    if PLOTTER_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

#######################################################################################################################
#######################################################################################################################