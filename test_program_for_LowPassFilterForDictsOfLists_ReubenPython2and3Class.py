# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision E, 09/07/2024

Verified working on: Python 3.8 for Windows 10 64-bit, Ubuntu 20.04, and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

###########################################################
from EntryListWithBlinking_ReubenPython2and3Class import *
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
import keyboard
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
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global EntryListWithBlinking_ReubenPython2and3ClassObject
    global EntryListWithBlinking_OPEN_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if EntryListWithBlinking_OPEN_FLAG == 1:
                EntryListWithBlinking_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        #################################################

    ##########################################################################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_Canon6dofFTsensorFH30020_ReubenPython3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

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
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 0

    global USE_LowPassFilterForDictsOfLists_FLAG
    USE_LowPassFilterForDictsOfLists_FLAG = 1

    global USE_EntryListWithBlinking_FLAG
    USE_EntryListWithBlinking_FLAG = 1

    global USE_PLOTTER_FLAG
    USE_PLOTTER_FLAG = 1

    global USE_SPECKLE_NOISE_FLAG
    USE_SPECKLE_NOISE_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global GUI_ROW_EntryListWithBlinking
    global GUI_COLUMN_EntryListWithBlinking
    global GUI_PADX_EntryListWithBlinking
    global GUI_PADY_EntryListWithBlinking
    global GUI_ROWSPAN_EntryListWithBlinking
    global GUI_COLUMNSPAN_EntryListWithBlinking
    GUI_ROW_EntryListWithBlinking = 1

    GUI_COLUMN_EntryListWithBlinking = 0
    GUI_PADX_EntryListWithBlinking = 1
    GUI_PADY_EntryListWithBlinking = 1
    GUI_ROWSPAN_EntryListWithBlinking = 1
    GUI_COLUMNSPAN_EntryListWithBlinking = 1
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

    global root

    global root_Xpos
    root_Xpos = 870

    global root_Ypos
    root_Ypos = 20

    global root_width
    root_width = 1020

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject

    global LowPassFilterForDictsOfLists_OPEN_FLAG
    LowPassFilterForDictsOfLists_OPEN_FLAG = -1

    global LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict
    LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict = dict()

    global LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda
    LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda = 0.5 #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

    global DesiredAngleDeg_1_Raw
    DesiredAngleDeg_1_Raw = 0.0
    
    global DesiredAngleDeg_1_Filtered
    DesiredAngleDeg_1_Filtered = 0.0

    global DesiredAngleDeg_2_Raw
    DesiredAngleDeg_2_Raw = 0.0

    global DesiredAngleDeg_2_Filtered
    DesiredAngleDeg_2_Filtered = 0.0
    ####################################################
    ####################################################

    #################################################
    #################################################
    global EntryListWithBlinking_ReubenPython2and3ClassObject

    global EntryListWithBlinking_OPEN_FLAG
    EntryListWithBlinking_OPEN_FLAG = -1

    global EntryListWithBlinking_MostRecentDict
    EntryListWithBlinking_MostRecentDict = dict()

    global EntryListWithBlinking_MostRecentDict_DataUpdateNumber
    EntryListWithBlinking_MostRecentDict_DataUpdateNumber = 0

    global EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last
    EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last = -1

    EntryWidth = 10
    LabelWidth = 60
    FontSize = 12
    #################################################
    #################################################

    ####################################################
    ####################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global PLOTTER_OPEN_FLAG
    PLOTTER_OPEN_FLAG = -1
    ####################################################
    ####################################################

    ####################################################  KEY GUI LINE
    ####################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_Canon6dofFTsensorFH30020 = None
        Tab_MyPrint = None
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    if USE_LowPassFilterForDictsOfLists_FLAG == 1:
        try:

            LowPassFilterForDictsOfLists_DictOfVariableFilterSettings = dict([("DesiredAngleDeg_1", dict([("UseMedianFilterFlag", 1), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda)])),
                                                                              ("DesiredAngleDeg_2", dict([("UseMedianFilterFlag", 0), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda)]))])

            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject = LowPassFilterForDictsOfLists_ReubenPython2and3Class(dict([("DictOfVariableFilterSettings", LowPassFilterForDictsOfLists_DictOfVariableFilterSettings)]))
            LowPassFilterForDictsOfLists_OPEN_FLAG = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("LowPassFilterForDictsOfLists_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    global EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict
    EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict = dict([("root", Tab_MainControls),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_EntryListWithBlinking),
                                    ("GUI_COLUMN", GUI_COLUMN_EntryListWithBlinking),
                                    ("GUI_PADX", GUI_PADX_EntryListWithBlinking),
                                    ("GUI_PADY", GUI_PADY_EntryListWithBlinking),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_EntryListWithBlinking),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_EntryListWithBlinking)])

    global EntryListWithBlinking_Variables_ListOfDicts
    EntryListWithBlinking_Variables_ListOfDicts = [dict([("Name", "LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda"),
                                                         ("Type", "float"),
                                                         ("StartingVal", LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda),
                                                         ("MinVal", 0.0),
                                                         ("MaxVal", 1.0),
                                                         ("EntryBlinkEnabled", 0),
                                                         ("EntryWidth", EntryWidth),
                                                         ("LabelWidth", LabelWidth),
                                                         ("FontSize", FontSize)])]

    global EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict
    EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                          ("EntryListWithBlinking_Variables_ListOfDicts", EntryListWithBlinking_Variables_ListOfDicts),
                                                                          ("DebugByPrintingVariablesFlag", 0),
                                                                          ("LoseFocusIfMouseLeavesEntryFlag", 0)])
    if USE_EntryListWithBlinking_FLAG == 1:
        try:
            EntryListWithBlinking_ReubenPython2and3ClassObject = EntryListWithBlinking_ReubenPython2and3Class(EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict)
            EntryListWithBlinking_OPEN_FLAG = EntryListWithBlinking_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("EntryListWithBlinking_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    ####################################################
    ####################################################

    ####################################################
    ####################################################
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
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["DesiredAngleDeg_1_Raw", "DesiredAngleDeg_1_Filtered", "DesiredAngleDeg_2_Raw", "DesiredAngleDeg_2_Filtered"]),("ColorList", ["Red", "Green", "Orange", "Blue"])])),
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
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    if USE_KEYBOARD_FLAG == 1:
        keyboard.on_press_key("esc", ExitProgram_Callback)
        #keyboard.on_press_key("space", ExitProgram_Callback)
        #keyboard.on_press_key("e", ExitProgram_Callback)
        keyboard.on_press_key("q", ExitProgram_Callback)
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    if LowPassFilterForDictsOfLists_OPEN_FLAG != 1:
        print("Failed to open LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.")
        #ExitProgram_Callback()
    ####################################################
    ####################################################

    #################################################
    #################################################
    if EntryListWithBlinking_OPEN_FLAG != 1:
        print("Failed to open EntryListWithBlinking_ReubenPython2and3Class.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PLOTTER_FLAG == 1 and PLOTTER_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterClass_Object.")
        #ExitProgram_Callback()
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
    while(EXIT_PROGRAM_FLAG == 0):

        ####################################################
        ####################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ####################################################
        ####################################################

        #################################################### GET's
        ####################################################
        if LowPassFilterForDictsOfLists_OPEN_FLAG == 1:

            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.GetMostRecentDataDict()
            #print("LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict: " + str(LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict))

            if "DesiredAngleDeg_1" in LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict:

                DesiredAngleDeg_1_Raw = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["DesiredAngleDeg_1"]["Raw_MostRecentValuesList"]
                DesiredAngleDeg_1_Filtered = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["DesiredAngleDeg_1"]["Filtered_MostRecentValuesList"]

                DesiredAngleDeg_2_Raw = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["DesiredAngleDeg_2"]["Raw_MostRecentValuesList"]
                DesiredAngleDeg_2_Filtered = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject_MostRecentDict["DesiredAngleDeg_2"]["Filtered_MostRecentValuesList"]

        ####################################################
        ####################################################

        ####################################################
        ####################################################

        ################################################### GET's
        if EntryListWithBlinking_OPEN_FLAG == 1:

            EntryListWithBlinking_MostRecentDict = EntryListWithBlinking_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "DataUpdateNumber" in EntryListWithBlinking_MostRecentDict and EntryListWithBlinking_MostRecentDict["DataUpdateNumber"] != EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last:
                EntryListWithBlinking_MostRecentDict_DataUpdateNumber = EntryListWithBlinking_MostRecentDict["DataUpdateNumber"]
                #print("DataUpdateNumber = " + str(EntryListWithBlinking_MostRecentDict_DataUpdateNumber) + ", EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))

                if EntryListWithBlinking_MostRecentDict_DataUpdateNumber > 1:
                    LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda = EntryListWithBlinking_MostRecentDict["LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda"]

                    if LowPassFilterForDictsOfLists_OPEN_FLAG == 1:
                        LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["DesiredAngleDeg_1"]["ExponentialSmoothingFilterLambda"] = LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda
                        #LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["DesiredAngleDeg_2"]["ExponentialSmoothingFilterLambda"] = LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda
                        LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddOrUpdateDictOfVariableFilterSettingsFromExternalProgram(LowPassFilterForDictsOfLists_DictOfVariableFilterSettings)

        ###################################################

        ###################################################
        EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last = EntryListWithBlinking_MostRecentDict_DataUpdateNumber
        ###################################################

        ####################################################
        ####################################################

        #################################################### SET's
        ####################################################
        if LowPassFilterForDictsOfLists_OPEN_FLAG == 1:
            time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
            DesiredAngleDeg_1_Calculated = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + 0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.sin(time_gain * CurrentTime_MainLoopThread)  #math.exp(0.1*CurrentTime_MainLoopThread)*0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) *
            DesiredAngleDeg_2_Calculated = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + 0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.cos(time_gain * CurrentTime_MainLoopThread)

            ####################################################
            if USE_SPECKLE_NOISE_FLAG == 1:
                NoiseCounter = NoiseCounter + 1
                if NoiseCounter == 1:
                    NoiseAmplitude = NoiseAmplitude_Percent0to1OfSinuisoidalInputAmplitude*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)
                    
                    NoiseValue_1 = random.uniform(-1.0*NoiseAmplitude, NoiseAmplitude)
                    DesiredAngleDeg_1_Calculated = DesiredAngleDeg_1_Calculated + NoiseValue_1
                    
                    NoiseValue_2 = random.uniform(-1.0*NoiseAmplitude, NoiseAmplitude)
                    DesiredAngleDeg_2_Calculated = DesiredAngleDeg_2_Calculated + NoiseValue_2
                    
                    NoiseCounter = 0
            ####################################################

            ####################################################
            LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDataDictFromExternalProgram(dict([("DesiredAngleDeg_1", [DesiredAngleDeg_1_Calculated]),
                                                                                                           ("DesiredAngleDeg_2", [DesiredAngleDeg_2_Calculated])]))
            ####################################################

        ####################################################
        ####################################################

        ####################################################
        ####################################################
        if PLOTTER_OPEN_FLAG == 1:
            try:
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

                    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["DesiredAngleDeg_1_Raw", "DesiredAngleDeg_1_Filtered", "DesiredAngleDeg_2_Raw", "DesiredAngleDeg_2_Filtered"],
                                                                                                                            [CurrentTime_MainLoopThread]*4,
                                                                                                                            [DesiredAngleDeg_1_Raw[0], DesiredAngleDeg_1_Filtered[0], DesiredAngleDeg_2_Raw[0], DesiredAngleDeg_2_Filtered[0]])

                ####################################################
            except:
                exceptions = sys.exc_info()[0]
                print("test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class: MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot, exceptions: %s" % exceptions, 0)
                traceback.print_exc()
        ####################################################
        ####################################################

        ####################################################
        ####################################################
        UpdateFrequencyCalculation()

        time.sleep(0.040)
        ####################################################
        ####################################################

    ####################################################
    ####################################################
    ####################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class.")

    #################################################
    if EntryListWithBlinking_OPEN_FLAG == 1:
        EntryListWithBlinking_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if PLOTTER_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

#######################################################################################################################
#######################################################################################################################