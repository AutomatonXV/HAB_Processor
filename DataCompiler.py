'''
Post Process into graphs
By Arnab Sinha (arnab.sinha@mail.mcgill.ca)
'''

import csv
import numpy as np
import pandas as pd

import os 
import matplotlib.pyplot as plt
import PlotAssist, EZColors
import Data

class Processor:
    def __init__(self, CSVName):
        self.CurrentFile = CSVName
        self.FullData = {}
        self.FullData["Time"] = []
        self.FullData["Pressure"] = []
        self.FullData["Temp0"] = []
        self.FullData["Temp1"] = []
        self.FullData["Temp2"] = []
        self.FullData["alt"] = []
        self.FullData["alt_real"] = []
        self.FullData["SL"] = []

        
    def getCompiled(self,):
        self.__tabulateCSV()
        return self.FullData
        
    def __tabulateCSV(self,):
        abspath = os.path.abspath('Data\\'+self.CurrentFile+".csv")
        print(abspath)
        file = open(abspath)
        reader = csv.reader(file)
        
        Iter = 0
        for row in reader:
            if Iter <= 1: Iter +=1 ; continue #skip header lines
            Time,Pressure,Temp0,Temp1,Temp2,alt,alt_real,SL = self.__correctFormat(row)
            self.FullData['Time'].append(Time)
            self.FullData['Pressure'].append(Pressure)
            self.FullData['Temp0'].append(Temp0)
            self.FullData['Temp1'].append(Temp1)
            self.FullData['Temp2'].append(Temp2)
            self.FullData['alt'].append(alt)
            self.FullData['alt_real'].append(alt_real)
            self.FullData['SL'].append(SL)
            Iter+=1

    def __correctFormat(self, row):
        newRow = []
        pos = 0
        for val in row[0:8]:
            pos +=1 
            #filtered = val[1:]
            filtered = np.float64(val.replace("'", ''))
            newRow.append(filtered)

        return int(newRow[0]), newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7]

    
            


        
        #rows = [list(row) for row in df.values]
        #print(rows)

