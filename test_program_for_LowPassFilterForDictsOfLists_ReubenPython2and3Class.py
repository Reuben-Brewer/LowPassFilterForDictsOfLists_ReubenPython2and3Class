# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision I, 12/22/2025

Verified working on: Python 3.11/12/13 for Windows 10/11 64-bit, Ubuntu 20.04, and Raspberry Pi Bookworm (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

#######################################################################################################################
#######################################################################################################################

###########################################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
###########################################################

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
import math
import numpy
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

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def GetLatestWaveformValue(CurrentTime, MinValue, MaxValue, Period, WaveformTypeString="Sine"):

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            ##########################################################################################################
            OutputValue = 0.0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            WaveformTypeString_ListOfAcceptableValues = ["Sine", "Cosine", "Triangular", "Square"]

            if WaveformTypeString not in WaveformTypeString_ListOfAcceptableValues:
                print("GetLatestWaveformValue: Error, WaveformTypeString must be in " + str(WaveformTypeString_ListOfAcceptableValues))
                return -11111.0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if WaveformTypeString == "Sine":

                TimeGain = math.pi/Period
                OutputValue = (MaxValue + MinValue)/2.0 + 0.5*abs(MaxValue - MinValue)*math.sin(TimeGain*CurrentTime)
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Cosine":

                TimeGain = math.pi/Period
                OutputValue = (MaxValue + MinValue)/2.0 + 0.5*abs(MaxValue - MinValue)*math.cos(TimeGain*CurrentTime)
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Triangular":
                TriangularInput_TimeGain = 1.0
                TriangularInput_MinValue = -5
                TriangularInput_MaxValue = 5.0
                TriangularInput_PeriodInSeconds = 2.0

                #TriangularInput_Height0toPeak = abs(TriangularInput_MaxValue - TriangularInput_MinValue)
                #TriangularInput_CalculatedValue_1 = abs((TriangularInput_TimeGain*CurrentTime_CalculatedFromMainThread % PeriodicInput_PeriodInSeconds) - TriangularInput_Height0toPeak) + TriangularInput_MinValue

                A = abs(MaxValue - MinValue)
                P = Period

                #https://stackoverflow.com/questions/1073606/is-there-a-one-line-function-that-generates-a-triangle-wave
                OutputValue = (A / (P / 2)) * ((P / 2) - abs(CurrentTime % (2 * (P / 2)) - P / 2)) + MinValue
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Square":

                TimeGain = math.pi/Period
                MeanValue = (MaxValue + MinValue)/2.0
                SinusoidalValue =  MeanValue + 0.5*abs(MaxValue - MinValue)*math.sin(TimeGain*CurrentTime)

                if SinusoidalValue >= MeanValue:
                    OutputValue = MaxValue
                else:
                    OutputValue = MinValue
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            else:
                OutputValue = 0.0
            ##########################################################################################################
            ##########################################################################################################

            return OutputValue

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        except:
            exceptions = sys.exc_info()[0]
            print("GetLatestWaveformValue: Exceptions: %s" % exceptions)
            return -11111.0
            traceback.print_exc()
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

    number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

    ListOfStringsToJoin = []

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if isinstance(input, str) == 1:
        ListOfStringsToJoin.append(input)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
        element = float(input)
        prefix_string = "{:." + str(number_of_decimal_places) + "f}"
        element_as_string = prefix_string.format(element)

        ##########################################################################################################
        ##########################################################################################################
        if element >= 0:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
            element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
        else:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
        ##########################################################################################################
        ##########################################################################################################

        ListOfStringsToJoin.append(element_as_string)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, list) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append(ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, tuple) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append("TUPLE" + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, dict) == 1:

        if len(input) > 0:
            for Key in input: #RECURSION
                ListOfStringsToJoin.append(str(Key) + ": " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a dict()
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    else:
        ListOfStringsToJoin.append(str(input))
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if len(ListOfStringsToJoin) > 1:

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        StringToReturn = ""
        for Index, StringToProcess in enumerate(ListOfStringsToJoin):

            ################################################
            if Index == 0: #The first element
                if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                    StringToReturn = "{"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                    StringToReturn = "("
                else:
                    StringToReturn = "["

                StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
            ################################################

            ################################################
            elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                StringToReturn = StringToReturn + StringToProcess + ", "
            ################################################

            ################################################
            else: #The last element
                StringToReturn = StringToReturn + StringToProcess

                if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                    StringToReturn = StringToReturn + "}"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                    StringToReturn = StringToReturn + ")"
                else:
                    StringToReturn = StringToReturn + "]"

            ################################################

        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    elif len(ListOfStringsToJoin) == 1:
        StringToReturn = ListOfStringsToJoin[0]

    else:
        StringToReturn = ListOfStringsToJoin

    return StringToReturn
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertDictToProperlyFormattedStringForPrinting(DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

    ProperlyFormattedStringForPrinting = ""
    ItemsPerLineCounter = 0

    for Key in DictToPrint:

        if isinstance(DictToPrint[Key], dict): #RECURSION
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 str(Key) + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 str(Key) + ": " + \
                                                 ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)

        if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
            ItemsPerLineCounter = ItemsPerLineCounter + 1
        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
            ItemsPerLineCounter = 0

    return ProperlyFormattedStringForPrinting
##########################################################################################################
##########################################################################################################

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
    global CurrentTime_CalculatedFromMainThread
    global LastTime_CalculatedFromMainThread
    global DataStreamingFrequency_CalculatedFromMainThread
    global DataStreamingDeltaT_CalculatedFromMainThread
    global Counter_CalculatedFromMainThread

    try:
        DataStreamingDeltaT_CalculatedFromMainThread = CurrentTime_CalculatedFromMainThread - LastTime_CalculatedFromMainThread

        if DataStreamingDeltaT_CalculatedFromMainThread != 0.0:
            DataStreamingFrequency_CalculatedFromMainThread = 1.0 / DataStreamingDeltaT_CalculatedFromMainThread

        LastTime_CalculatedFromMainThread = CurrentTime_CalculatedFromMainThread
        Counter_CalculatedFromMainThread = Counter_CalculatedFromMainThread + 1

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

    global EntryListWithBlinking_Object
    global EntryListWithBlinking_OPEN_FLAG

    if USE_GUI_FLAG == 1:
        
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if EntryListWithBlinking_OPEN_FLAG == 1:
                EntryListWithBlinking_Object.GUI_update_clock()
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
#######################################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    global EntryListWithBlinking_Object
    global EntryListWithBlinking_OPEN_FLAG

    ####################################################################################################################### KEY GUI LINE
    #######################################################################################################################
    root = Tk()
    
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    #######################################################################################################################
    #######################################################################################################################

    #######################################################################################################################
    #######################################################################################################################
    global TabControlObject
    global Tab_MainControls

    if USE_TABS_IN_GUI_FLAG == 1:
        #######################################################################################################################
        TabControlObject = ttk.Notebook(root)

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############

        #######################################################################################################################
    else:
        #######################################################################################################################
        Tab_MainControls = root
        #######################################################################################################################

    #######################################################################################################################
    #######################################################################################################################

    #######################################################################################################################
    #######################################################################################################################
    if EntryListWithBlinking_OPEN_FLAG == 1:
        EntryListWithBlinking_Object.CreateGUIobjects(TkinterParent=Tab_MainControls)
    #######################################################################################################################
    #######################################################################################################################

    ####################################################################################################################### THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    #######################################################################################################################
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #######################################################################################################################
    #######################################################################################################################

    ####################################################################################################################### THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    #######################################################################################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #######################################################################################################################
    #######################################################################################################################

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

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

    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    USE_MyPlotterPureTkinterStandAloneProcess_FLAG = 1

    global USE_SPECKLE_NOISE_FLAG
    USE_SPECKLE_NOISE_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1

    global USE_PauseAndRequireInputBetweenEachLoopCountForDebugging_FLAG #unicorn
    USE_PauseAndRequireInputBetweenEachLoopCountForDebugging_FLAG = 0
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

    global CurrentTime_CalculatedFromMainThread
    CurrentTime_CalculatedFromMainThread = -11111.0

    global LastTime_CalculatedFromMainThread
    LastTime_CalculatedFromMainThread = -11111.0

    global DataStreamingFrequency_CalculatedFromMainThread
    DataStreamingFrequency_CalculatedFromMainThread = -11111.0

    global DataStreamingDeltaT_CalculatedFromMainThread
    DataStreamingDeltaT_CalculatedFromMainThread = -11111.0

    global StartingTime_CalculatedFromMainThread
    StartingTime_CalculatedFromMainThread = -1

    global Counter_CalculatedFromMainThread
    Counter_CalculatedFromMainThread = 0

    global PeriodicInput_AcceptableValues
    PeriodicInput_AcceptableValues = ["GUI", "Sine", "Cosine", "Triangular", "Square"]

    global PeriodicInput_Type_1
    PeriodicInput_Type_1 = "Sine"

    global PeriodicInput_MinValue_1
    PeriodicInput_MinValue_1 = -1.0

    global PeriodicInput_MaxValue_1
    PeriodicInput_MaxValue_1 = 1.0

    global PeriodicInput_Period_1
    PeriodicInput_Period_1 = 1.0

    global PeriodicInput_CalculatedValue_1
    PeriodicInput_CalculatedValue_1 = 0.0

    global PeriodicInput_Type_2
    PeriodicInput_Type_2 = "Sine"

    global PeriodicInput_MinValue_2
    PeriodicInput_MinValue_2 = -1.0

    global PeriodicInput_MaxValue_2
    PeriodicInput_MaxValue_2 = 1.0

    global PeriodicInput_Period_2
    PeriodicInput_Period_2 = 1.0

    global PeriodicInput_CalculatedValue_2
    PeriodicInput_CalculatedValue_2 = 0.0

    global NoiseCounter
    NoiseCounter = 0

    global NoiseCounter_FireEveryNth
    NoiseCounter_FireEveryNth = 5

    global NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude
    NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude = 0.25
    
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
    global LowPassFilterForDictsOfLists_Object

    global LowPassFilterForDictsOfLists_OPEN_FLAG
    LowPassFilterForDictsOfLists_OPEN_FLAG = -1

    global LowPassFilterForDictsOfLists_MostRecentDict
    LowPassFilterForDictsOfLists_MostRecentDict = dict()

    global LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda  #unicorn
    LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda = 0.7 #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

    global LowPassFilterForDictsOfLists_UseMedianFilterFlag
    LowPassFilterForDictsOfLists_UseMedianFilterFlag = 0

    global LowPassFilterForDictsOfLists_UseExponentialSmoothingFilterFlag
    LowPassFilterForDictsOfLists_UseExponentialSmoothingFilterFlag = 1

    global LowPassFilterForDictsOfLists_AddDataDictFromExternalProgram__PrintInfoForDebuggingFlag
    LowPassFilterForDictsOfLists_AddDataDictFromExternalProgram__PrintInfoForDebuggingFlag = 0
    ####################################################
    ####################################################

    #################################################
    #################################################
    global EntryListWithBlinking_Object

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
    global MyPlotterPureTkinterStandAloneProcess_Object

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = -1

    global LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess
    LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess = -11111.0
    ####################################################
    ####################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ####################################################
    ####################################################
    if USE_LowPassFilterForDictsOfLists_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:

            LowPassFilterForDictsOfLists_DictOfVariableFilterSettings = dict([("PeriodicInput_CalculatedValue_1", dict([("UseMedianFilterFlag", LowPassFilterForDictsOfLists_UseMedianFilterFlag), ("UseExponentialSmoothingFilterFlag", LowPassFilterForDictsOfLists_UseExponentialSmoothingFilterFlag),("ExponentialSmoothingFilterLambda", LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda)])),
                                                                              ("PeriodicInput_CalculatedValue_2", dict([("UseMedianFilterFlag", LowPassFilterForDictsOfLists_UseMedianFilterFlag), ("UseExponentialSmoothingFilterFlag", LowPassFilterForDictsOfLists_UseExponentialSmoothingFilterFlag),("ExponentialSmoothingFilterLambda", LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda)]))])

            LowPassFilterForDictsOfLists_Object = LowPassFilterForDictsOfLists_ReubenPython2and3Class(dict([("DictOfVariableFilterSettings", LowPassFilterForDictsOfLists_DictOfVariableFilterSettings)]))
            LowPassFilterForDictsOfLists_OPEN_FLAG = LowPassFilterForDictsOfLists_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("LowPassFilterForDictsOfLists_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
    ####################################################
    ####################################################

    #################################################
    #################################################
    if USE_LowPassFilterForDictsOfLists_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if LowPassFilterForDictsOfLists_OPEN_FLAG != 1:
                print("Failed to open LowPassFilterForDictsOfLists_ReubenPython2and3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global EntryListWithBlinking_GUIparametersDict
    EntryListWithBlinking_GUIparametersDict = dict([("UseBorderAroundThisGuiObjectFlag", 0),
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
                                                         ("FontSize", FontSize)]),
                                                   dict([("Name", "LowPassFilterForDictsOfLists_UseMedianFilterFlag"),
                                                         ("Type", "int"),
                                                         ("StartingVal", LowPassFilterForDictsOfLists_UseMedianFilterFlag),
                                                         ("MinVal", 0.0),
                                                         ("MaxVal", 1.0),
                                                         ("EntryBlinkEnabled", 0),
                                                         ("EntryWidth", EntryWidth),
                                                         ("LabelWidth", LabelWidth),
                                                         ("FontSize", FontSize)])]

    global EntryListWithBlinking_SetupDict
    EntryListWithBlinking_SetupDict = dict([("GUIparametersDict", EntryListWithBlinking_GUIparametersDict),
                                              ("EntryListWithBlinking_Variables_ListOfDicts", EntryListWithBlinking_Variables_ListOfDicts),
                                              ("DebugByPrintingVariablesFlag", 0),
                                              ("LoseFocusIfMouseLeavesEntryFlag", 0)])

    if USE_EntryListWithBlinking_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            EntryListWithBlinking_Object = EntryListWithBlinking_ReubenPython2and3Class(EntryListWithBlinking_SetupDict)
            EntryListWithBlinking_OPEN_FLAG = EntryListWithBlinking_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("EntryListWithBlinking_Object __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_EntryListWithBlinking_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if EntryListWithBlinking_OPEN_FLAG != 1:
                print("Failed to open EntryListWithBlinking_ReubenPython2and3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                    ("NumberOfPrintLines", 10),
                                                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                    ("GraphCanvasWidth", 890),
                                                                    ("GraphCanvasHeight", 700),
                                                                    ("GraphCanvasWindowStartingX", 0),
                                                                    ("GraphCanvasWindowStartingY", 0),
                                                                    ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 30)])

    global MyPlotterPureTkinterStandAloneProcess_SetupDict
    MyPlotterPureTkinterStandAloneProcess_SetupDict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_GUIparametersDict),
                                                            ("ParentPID", os.getpid()),
                                                            ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 5.0),
                                                            ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["PeriodicInput_CalculatedValue_1_Raw", "PeriodicInput_CalculatedValue_1_Filtered", "PeriodicInput_CalculatedValue_2_Raw", "PeriodicInput_CalculatedValue_2_Filtered"]),
                                                                                                            ("MarkerSizeList", [3, 3, 3, 3]),
                                                                                                            ("LineWidthList", [3, 3, 3, 3]),
                                                                                                            ("ColorList", ["Red", "Green", "Orange", "Blue"])])),
                                                            ("SmallTextSize", 7),
                                                            ("LargeTextSize", 12),
                                                            ("NumberOfDataPointToPlot", 50),
                                                            ("XaxisNumberOfTickMarks", 10),
                                                            ("YaxisNumberOfTickMarks", 10),
                                                            ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("XaxisAutoscaleFlag", 1),
                                                            ("YaxisAutoscaleFlag", 1),
                                                            ("X_min", 0.0),
                                                            ("X_max", 20.0),
                                                            ("Y_min", 1.1*min(PeriodicInput_MinValue_1, PeriodicInput_MinValue_2)),
                                                            ("Y_max", 1.1*max(PeriodicInput_MinValue_1, PeriodicInput_MinValue_2)),
                                                            ("XaxisDrawnAtBottomOfGraph", 0),
                                                            ("XaxisLabelString", "Time (sec)"),
                                                            ("YaxisLabelString", "Y-units (units)"),
                                                            ("ShowLegendFlag", 1),
                                                            ("SavePlot_DirectoryPath", os.path.join(os.getcwd(), "SavedImagesFolder"))])

    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPlotterPureTkinterStandAloneProcess_Object = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_SetupDict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
                print("Failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################  KEY GUI LINE
    ##########################################################################################################
    ##########################################################################################################
    if USE_GUI_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread, daemon=True) #Daemon=True means that the GUI thread is destroyed automatically when the main thread is destroyed
        GUI_Thread_ThreadingObject.start()
    else:
        root = None
        Tab_MainControls = None
        Tab_MyPrint = None
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if EXIT_PROGRAM_FLAG == 0:
        StartingTime_CalculatedFromMainThread = getPreciseSecondsTimeStampString()
        print("Starting 'test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class.py")
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    random.seed() #IMPORTANT
    while(EXIT_PROGRAM_FLAG == 0):

        #################################################
        #################################################
        CurrentTime_CalculatedFromMainThread = getPreciseSecondsTimeStampString() - StartingTime_CalculatedFromMainThread
        #################################################
        #################################################

        ################################################# GET's
        #################################################

        ##################################################
        if EntryListWithBlinking_OPEN_FLAG == 1:

            EntryListWithBlinking_MostRecentDict = EntryListWithBlinking_Object.GetMostRecentDataDict()

            if "DataUpdateNumber" in EntryListWithBlinking_MostRecentDict and EntryListWithBlinking_MostRecentDict["DataUpdateNumber"] != EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last:
                EntryListWithBlinking_MostRecentDict_DataUpdateNumber = EntryListWithBlinking_MostRecentDict["DataUpdateNumber"]
                #print("DataUpdateNumber = " + str(EntryListWithBlinking_MostRecentDict_DataUpdateNumber) + ", EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))

                if EntryListWithBlinking_MostRecentDict_DataUpdateNumber > 1:
                    LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda = EntryListWithBlinking_MostRecentDict["LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda"]
                    LowPassFilterForDictsOfLists_UseMedianFilterFlag = EntryListWithBlinking_MostRecentDict["LowPassFilterForDictsOfLists_UseMedianFilterFlag"]

                    if LowPassFilterForDictsOfLists_OPEN_FLAG == 1:
                        LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["PeriodicInput_CalculatedValue_1"]["ExponentialSmoothingFilterLambda"] = LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda
                        LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["PeriodicInput_CalculatedValue_2"]["ExponentialSmoothingFilterLambda"] = LowPassFilterForDictsOfLists_ExponentialSmoothingFilterLambda

                        LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["PeriodicInput_CalculatedValue_1"]["UseMedianFilterFlag"] = LowPassFilterForDictsOfLists_UseMedianFilterFlag
                        LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["PeriodicInput_CalculatedValue_2"]["UseMedianFilterFlag"] = LowPassFilterForDictsOfLists_UseMedianFilterFlag

                        LowPassFilterForDictsOfLists_Object.AddOrUpdateDictOfVariableFilterSettingsFromExternalProgram(LowPassFilterForDictsOfLists_DictOfVariableFilterSettings)

        #################################################

        #################################################
        EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last = EntryListWithBlinking_MostRecentDict_DataUpdateNumber
        #################################################

        #################################################
        #################################################

        #################################################
        #################################################

        #################################################
        PeriodicInput_CalculatedValue_1 = GetLatestWaveformValue(CurrentTime_CalculatedFromMainThread, 
                                                                PeriodicInput_MinValue_1, 
                                                                PeriodicInput_MaxValue_1, 
                                                                PeriodicInput_Period_1, 
                                                                PeriodicInput_Type_1)
        #################################################

        #################################################
        PeriodicInput_CalculatedValue_2 = PeriodicInput_CalculatedValue_1*2.0 + 3.0
        #################################################

        #################################################
        if USE_SPECKLE_NOISE_FLAG == 1:
            
            NoiseCounter = NoiseCounter + 1
            if NoiseCounter == NoiseCounter_FireEveryNth:
                NoiseAmplitude = NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude * abs(PeriodicInput_MaxValue_1 - PeriodicInput_MinValue_1)
                NoiseValue = random.uniform(-1.0 * NoiseAmplitude, NoiseAmplitude)
                PeriodicInput_CalculatedValue_2 = PeriodicInput_CalculatedValue_2 + NoiseValue
                NoiseCounter = 0
        #################################################
        
        #################################################
        #################################################

        ################################################# GET's and SET's
        #################################################
        if LowPassFilterForDictsOfLists_OPEN_FLAG == 1:

            '''
            #AddDataDictFromExternalProgram returns the same as GetMostRecentDataDict: return deepcopy(self.VariablesDict.copy()), SO THERE'S NO NEED TO CALL LowPassFilterForDictsOfLists_MostRecentDict SEPARATELY.
            #LowPassFilterForDictsOfLists_MostRecentDict = LowPassFilterForDictsOfLists_Object.GetMostRecentDataDict() 
            #print("LowPassFilterForDictsOfLists_MostRecentDict: " + str(LowPassFilterForDictsOfLists_MostRecentDict))
            '''

            LowPassFilterForDictsOfLists_MostRecentDict = LowPassFilterForDictsOfLists_Object.AddDataDictFromExternalProgram(dict([("PeriodicInput_CalculatedValue_1", [PeriodicInput_CalculatedValue_1]),
                                                                                                                                   ("PeriodicInput_CalculatedValue_2", [PeriodicInput_CalculatedValue_2])]),
                                                                                                                                   PrintInfoForDebuggingFlag=LowPassFilterForDictsOfLists_AddDataDictFromExternalProgram__PrintInfoForDebuggingFlag)

            if "PeriodicInput_CalculatedValue_1" in LowPassFilterForDictsOfLists_MostRecentDict:
                PeriodicInput_CalculatedValue_1_Raw = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_1"]["Raw_MostRecentValuesList"] #USUALLY WHAT YOU WANT.
                PeriodicInput_CalculatedValue_1_Filtered = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_1"]["Filtered_MostRecentValuesList"] #USUALLY WHAT YOU WANT.

                PeriodicInput_CalculatedValue_1__SignalInRawHistoryList = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_1"]["__SignalInRawHistoryList"] #YOU USUALLY DON'T WANT TO LOOK AT THIS HISTORY LIST; LOOKING HERE JUST FOR DEBUGGING
                PeriodicInput_CalculatedValue_1__SignalOutFilteredHistoryList = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_1"]["__SignalOutFilteredHistoryList"] #YOU USUALLY DON'T WANT TO LOOK AT THIS HISTORY LIST; LOOKING HERE JUST FOR DEBUGGING

                PeriodicInput_CalculatedValue_2_Raw = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_2"]["Raw_MostRecentValuesList"] #USUALLY WHAT YOU WANT.
                PeriodicInput_CalculatedValue_2_Filtered = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_2"]["Filtered_MostRecentValuesList"] #USUALLY WHAT YOU WANT.

                PeriodicInput_CalculatedValue_2__SignalInRawHistoryList = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_2"]["__SignalInRawHistoryList"] #YOU USUALLY DON'T WANT TO LOOK AT THIS HISTORY LIST; LOOKING HERE JUST FOR DEBUGGING
                PeriodicInput_CalculatedValue_2__SignalOutFilteredHistoryList = LowPassFilterForDictsOfLists_MostRecentDict["PeriodicInput_CalculatedValue_2"]["__SignalOutFilteredHistoryList"] #YOU USUALLY DON'T WANT TO LOOK AT THIS HISTORY LIST; LOOKING HERE JUST FOR DEBUGGING

                if LowPassFilterForDictsOfLists_AddDataDictFromExternalProgram__PrintInfoForDebuggingFlag == 1:
                    print("***"
                          "\nPeriodicInput_CalculatedValue_1_Raw: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_1_Raw, 0, 3) + \
                          "\nPeriodicInput_CalculatedValue_1_Fil: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_1_Filtered, 0, 3) + \

                          "\nHistory_1_Raw: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_1__SignalInRawHistoryList, 0, 3) + \
                          "\nHistory_1_Fil: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_1__SignalOutFilteredHistoryList, 0, 3) + \

                          "\nPeriodicInput_CalculatedValue_2_Raw: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_2_Raw, 0, 3) + \
                          "\nPeriodicInput_CalculatedValue_2_Fil: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_2_Filtered, 0, 3) + \

                          "\nHistory_2_Raw: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_2__SignalInRawHistoryList, 0, 3) + \
                          "\nHistory_2_Fil: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PeriodicInput_CalculatedValue_2__SignalOutFilteredHistoryList, 0, 3) + \

                          "\n***")

        #################################################

        #################################################
        #################################################

        #################################################
        #################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            #################################################
            try:

                MyPlotterPureTkinterStandAloneProcess_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_Object.GetMostRecentDataDict()

                if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_MostRecentDict:
                    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                    if MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag == 1:
                        if CurrentTime_CalculatedFromMainThread - LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess >= MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents"]/1000.0 + 0.001:
                            MyPlotterPureTkinterStandAloneProcess_Object.ExternalAddPointOrListOfPointsToPlot(["PeriodicInput_CalculatedValue_1_Raw",
                                                                                                             "PeriodicInput_CalculatedValue_1_Filtered",
                                                                                                             "PeriodicInput_CalculatedValue_2_Raw",
                                                                                                             "PeriodicInput_CalculatedValue_2_Filtered"],
                                                                                                            [CurrentTime_CalculatedFromMainThread]*4,
                                                                                                            [PeriodicInput_CalculatedValue_1_Raw,
                                                                                                             PeriodicInput_CalculatedValue_1_Filtered,
                                                                                                             PeriodicInput_CalculatedValue_2_Raw,
                                                                                                             PeriodicInput_CalculatedValue_2_Filtered])

                            LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess = CurrentTime_CalculatedFromMainThread

            #################################################

            #################################################
            except:
                exceptions = sys.exc_info()[0]
                print("test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class: MyPlotterPureTkinterStandAloneProcess_Object.ExternalAddPointOrListOfPointsToPlot, exceptions: %s" % exceptions, 0)
                traceback.print_exc()
            #################################################

        #################################################
        #################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        if USE_PauseAndRequireInputBetweenEachLoopCountForDebugging_FLAG == 1:
            input("Press to enter the next loop cycle.")

        UpdateFrequencyCalculation()

        time.sleep(0.030)
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    ##########################################################################################################
    print("Exiting 'test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class.py")

    #################################################
    #################################################
    #Nothing required to close LowPassFilterForDictsOfLists_ReubenPython2and3Class.
    #################################################
    #################################################

    #################################################
    #################################################
    if EntryListWithBlinking_OPEN_FLAG == 1:
        EntryListWithBlinking_Object.ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_Object.ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################