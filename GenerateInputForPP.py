import csv 
import sys

headArray = ['OP','HP','LP','CP']
header=""
splitCol=20

def readRowByRow(reader):
    rows = ""    
    colSymbol = ""
    index = 1    
    for row in reader:
        if index == 1:
            index+=1
            continue

        result = ""
        if colSymbol != row[0]:
            colSymbol = row[0]
            result+="\n"+colSymbol

        for col in row:
            if colSymbol != col:                
                result += "," +col
        rows += result

        index+=1
    return rows

def getHeader(index):
    header=""
    colLengh = (splitCol/len(headArray))
    while index <= colLengh:
        for headCol in headArray:
            header += ","+headCol + "_T-"+str(index)        
        index+=1
        if index > splitCol:
            break
    return header
#import pandas as pd
import os

resultContents=""
path = "inputFiles"
for fileName in os.listdir(path):
    with open(path+"\\"+fileName, mode='r', newline='') as File:          
        reader = csv.reader(File)    
        result = readRowByRow(reader)    
        index = 1
        header = getHeader(index)
        symbolArr = result.split(",")
        symbol = symbolArr[0].split("\n")    
        stock = symbol[1]
        result = stock
        prefix = ""
        for item in symbolArr:
            if symbolArr[0] == item: continue        
            result += prefix+","+item        
            if index == splitCol:
                prefix="\n"+stock
                index = 0     
            else:
                prefix=""
            index += 1   
    resultContents += "\n"+result

resultContents = 'Symbol'+ header+resultContents
with open("output.csv", mode='w', newline='') as csvFile:        
    csvFile.write(resultContents)