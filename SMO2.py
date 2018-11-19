#Simple SMO algorithm using a random dataSet

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

def smo1(dataMat, classLabels,C tolerance,iterations):
    dataMatrix = mat(dataMat); labelMatrix = mat(classLabels)
    b=0; m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))
    it=0
    while(it<iterations):
        alphaPairsCged = 0
        for i in range(m):
            fXi = float(multiply(alphas,labelMatrix).T*\
                        (dataMatrix*dataMatrix[i,:].T))+b
            Ei = fXi - float(labelMatrix[i])
            if((labelMat[i]*Ei<-tolerance) and (alphas[i]<C)) or \
               ((labelMatrix[i]*Ei>tolerance) and \
                (alphas[i]>0)):
                j = selectJrand(i,m)
                fXj = float(multiply(alphas,labelMatrix).T*\
                            (dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMatrix[j])
                alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy();
                if(labelMatrix[i]!=labelMatrix[j]):
                    L = max(0,alphas[j] - alphas[i])
                    H = min(C,C+alphas[j] - alphas[i])
                else:
                    L = max(0,alphas[j]+alphas[i]-C)
                    H = min(C,alphas[j]+alphas[i])
                if L==H:print "L==H"; continue
                eta = 2.0*dataMatrix[i,:]*dataMatrix[j,:].T - \
                      dataMatrix[i,:]*dataMatrix[i,:].T - \
                      dataMatrix[j,:]*dataMatrix[j,:].T
                if eta>=0: print "eta>=0"; continue
                alphas[j]-=labelMatrix[j]*(Ei-Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if(abs(alphas[j]-alphaJold)<0.00001):print\
                                                        "j is not moving fast"
                alphas[i]+=labelmatrix[j]*labelMatrix[i]*\
                            (alphaJold - alphas[j])
                b1 = b-Ei-labelMatrix[i]*(alphas[i]-alphaIold)*\
                     dataMatrix[i,:]*dataMatrix[i,:].T - \
                     labelMatrix[j]*(alphas[j] - alphaJold)*\
                     dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b-Ej-labelMatrix[i]*(alphas[i]-alphaIold)*\
                     dataMatrix[i,:]*dataMatrix[i,:].T - \
                     labelMatrix[j]*(alphas[j] - alphaJold)*\
                     dataMatrix[i,:]*dataMatrix[j,:].T
                if(0<alphas[i]) and (C>alphas[i]): b = b1
                elif (0<alphas[j]) and (C>alphas[j]): b=b2
                else: b = (b1+b2)/2.0
                alphaPairsChd+=1
                print "iter: %d i:%d, pairs changed %d" %\
                      (it,i,alphaPairsCgd)
        if(alphaPairsCgd==0):it+=1
        else: it=0
        print "iternation number: %d" %it
    return b,alphas

    
    
                                                
