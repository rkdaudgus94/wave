import matplotlib.pyplot as plt
import numpy as np
from drawnow import *

fig = plt.figure(1)
 
angles = []
sines = []
cosines = []
 
def show_plot():
    plt.plot(angles,sines,label='Sine')
    plt.plot(angles,cosines,label='Cosine')
    plt.legend()
    plt.grid()
    plt.xlabel('Angles [deg]')
    plt.ylabel('Value')
    
for x in np.linspace(0,np.pi*2,100):
    angles = np.append(angles, x)
    sines  = np.append(sines, np.sin(x))
    cosines= np.append(cosines, np.cos(x))
    
    drawnow(show_plot)