import numpy as np
from scipy import *
import pyparsing
import matplotlib.pyplot as plt
#plt.plot([1,2,3])
#plt.ylabel('some numbers')
#a=np.linspace(0,2*np.pi,50)
#plt.plot(a,np.sin(a),'r-o')
#plt.show()
#help(plt.plot)
x=np.linspace(0,2*pi,50)
y=sin(x)
z=cos(x)
plt.figure()
plt.scatter(x,y)
#plt.figure()
plt.scatter(x,z)
plt.show()

