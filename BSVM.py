#Basic Support Vector Machine
#DataSet used here is small

#Forming the dataSet
#This can also be done using a Pandas DataFrame

from numpy import *
def loadDataSet():
    dM = []
    Lm = []
    fr = open(' ') #Substitute a filename
    for line in fr.readlines():
        lineArray = line.strip().split('\t')
        dM.append([float(lineArray[0]),float(lineArray[1])])
        Lm.append(float(lineArray[2]))
    return dM, Lm

def selectJrand(i,m):
    j=i
    while(j==i):
        j = int(random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):
    if aj>H:
        aj=H
    if L>aj:
        aj=L
    return aj


