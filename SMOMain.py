#Full Platt SMO algorithm
class Optimal:
    def __init__(self,dataMatInput,classLabels,C,tolerance):
        self.X = dataMatInput
        self.labelMatrix = classLabels
        self.C = C
        self.toler = tolerance
        self.m = shape(dataMatInput)[0]
        self.alphas = mat(zeros((self.m,1)))
        self.b = 0
        self.eCache = mat(zeros((self.m,2)))

def calculateEk(oS1,k):
    fXk = float(multiply(oS1.alphas,oS1.labelMatrix).T*\
                (oS1.X*oS1.X[k,:].T)) + oS1.b
    Ek = fXk - float(oS1.labelMatrix[k])
    return Ek

def sJ(i,oS1,Ei):
    maxK = -1; maxDeltaE = 0; Ej=0
    oS1.eCache[i] = [1,Ei]
    validEcacheList = nonzero(oS1.eCache[:,0].A)[0]
    if(len(validEcacheList))>1:
        for k in validEcacheList:
            if k==i: continue
            Ek = calculateEk(oS1,k)
            deltaE = abs(Ei-Ek)
            if (deltaE>maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej=Ek
        return maxK,Ej
    else:
        j = selectJrand(i,oS1.m)
        Ej = calculateEk(oS,j)
    return j,Ej

def updateEk(oS,k):
    Ek = calculate(oS,k)
    oS.eCache[k] = [1,Ek]
    
def smonew(dataMatIn,LabelMat,C,tole,maxIter,kTup=('lin',0)):
    oS1 = optstruct(mat(dataMatIn),mat(LabelMat).transpose(),C,tole)
    it = 0
    FullSet=True; alphaPairsCgd = 0
    while(it<maxiters) and ((alphaPairsCgd>0) or (FullSet)):
        alphaPairsCgd = 0
        if FullSet:
            for i in range(oS1.m):
                alphaPairsCgd+=innerloop(i,oS1)
            print "FullSet, iter: %d i:%d, pairs changed %d" %(it,i,alphaPairs)
            it+=1
        else:
            nonBoundis = nonzero((oS1.alphas.A>0)*(oS1.alphas.A<C))[0]
            for i in nonBoundIs:
                alphaPairsCgd+=innerLoop(i,oS) #Simple SMO Algorithm
                print "non-Bound, iter"
            it+=1
        if FullSet: FullSet=False
        elif (alphaPairsCgd==0):entireSet=True
        print "iteration Number"
    return oS1.b,oS1.alphas
