import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *


N = 100000
t = linspace(0,100,N)


#### - Constants
D = 183888
ke  = 0.1
kd = 0.0867
ce = 0.57
cd = 0.43
me = ce*D-500*ke
md = cd*D-1820483*kd

#M = 
Stations = [4.71,3.83,3.6,6.12,3.35]
Chargers = [8288.76,9708.31,5265.85,5083.84,7577.72]
AADTT = [14288,12735,9843,9429,13975]
Air = [[8.4,7.9],[6.6,6.8,9.3],[9.2,8.1,6.6,7.2,6.3],[7.4,8.3,7.4,6.9],[12.8]]
weights = [0.78,0.27,0.23,0.71,0.04]


def getE(S,C):
    Econ = [0,0,0,0,0]
    cs = max(S)
    cc = max(C)
    for i in range(len(Econ)):
        Econ[i] = (S[i]/cs + C[i]/cc)/2
    return Econ

def getN(T,A):
    Enviro = [0,0,0,0,0]
    X = [0,0,0,0,0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            X[i] += A[i][j]/len(A[i])
    ct = max(T)
    ca = max(X)
    for i in range(len(Enviro)):
        avg = 0
        Enviro[i] = (T[i]/ct+X[i]/ca)/2
    return Enviro

def getScore3(S,C,T,A,we,r,n):
    ret = [0,0,0,0,0]
    wn = [0,0,0,0,0]
    for i in range(5):
        wn[i] = 1 - we[i]
    if(n==3):
        for i in range(5):
            ret[i] = we[i]*r/(we[i]*r+wn[i])*getE(S,C)[i]+wn[i]/(we[i]*r+wn[i])*getN(T,A)[i]
    if(n==4):
        for i in range(5):
            ret[i] = we[i]/(we[i]+wn[i]*r)*getE(S,C)[i]+wn[i]*r/(we[i]+wn[i]*r)*getN(T,A)[i]
    if(n==0):
        for i in range(5):
            ret[i] = we[i]*getE(S,C)[i]+wn[i]*getN(T,A)[i]
    return ret

p = 0.1
percentages = [[0,0,0,0,0],[0,0,0,0,0]]
for i in range(5):
    percentages[0][i] = getScore3(Stations,Chargers,AADTT,Air,weights,1-p,4)[i]/getScore3(Stations,Chargers,AADTT,Air,weights,1,0)[i]
    percentages[1][i] = getScore3(Stations,Chargers,AADTT,Air,weights,1+p,4)[i]/getScore3(Stations,Chargers,AADTT,Air,weights,1,0)[i]

print("wd")    
print(percentages)