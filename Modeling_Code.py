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

def getTe(t):
    return -me*exp(-ke*t)/ke+ce*D/ke

def getTd(t):
    return -md*exp(-kd*t)/kd+cd*D/kd

def getPercentA(a,b):
    return a/(a+b)*100

p = 0.1
values = [5,10,20]
outputs = [[0,0,0],[0,0,0]]
for i in range(len(values)):
    va = getPercentA(getTe(values[i]),getTd(values[i]))
    md *= (1-p)
    vb = getPercentA(getTe(values[i]),getTd(values[i]))
    outputs[0][i] = (vb-va)/va-mod((vb-va)/va,0.0001)
    md *= (1+p)/(1-p)
    vc = getPercentA(getTe(values[i]),getTd(values[i]))
    outputs[1][i] = (vc-va)/va-mod((vc-va)/va,0.0001)
    
print("md")
print(outputs)

rcParams["axes.grid"] = True
rcParams['font.size'] = 14
rcParams['axes.labelsize'] = 18

figure()
subplot(211)

plot(t,getPercentA(getTe(t),getTd(t)))

ylabel("Percent of electric trucks")

xlabel("Time (years)")
axes = plt.gca()
axes.set_xlim([0,25])
axes.set_ylim([0,100])

a = getPercentA(getTe(5),getTd(5))
b = getPercentA(getTe(10),getTd(10))
c = getPercentA(getTe(20),getTd(20))
types = [a-mod(a,0.001),b-mod(b,0.001),c-mod(c,0.001)]
x_coords = [5, 10, 20]
y_coords = [getPercentA(getTe(5),getTd(5)),getPercentA(getTe(10),getTd(10)),getPercentA(getTe(20),getTd(20))]


for i,type in enumerate(types):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y, marker='x', color='red') 
    plt.text(x-1, y+2.5, type, fontsize=9)

figure()
subplot(211)

axes = plt.gca()
axes.set_xlim([0,25])

plot(t,getTe(t), label="Electric Trucks")
plot(t,getTd(t), label="Diesel Trucks")
plot(t, getTe(t) + getTd(t), label = "Sum")


xlabel("Time (years)")
ylabel("Number of Trucks")

rcParams['legend.fontsize'] = 16.0
legend(loc=(0.1,-1),ncol=3)


#show()


tight_layout()
