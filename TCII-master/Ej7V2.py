# MÃ³dulos para Jupyter
from scipy import signal
import matplotlib.pyplot as plt

import numpy as np



R=1000 #ohms
C=10**(-6) #faradios
Rn=R/1000 
wn=1000
Cn=(C*wn*R)
start_omega = 10**-2 # r/s
stop_omega = 10**2 # r/s
cant_puntos= 10000 # puntos
omega=np.linspace( start_omega, stop_omega , cant_puntos)
sys = signal.TransferFunction([-Cn*Rn,1], [Cn*Rn,1])
w, mag, phase = signal.bode(sys,omega)

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.ylim([-1,1])

plt.figure() 
plt.semilogx(w, phase)  # Bode phase plot
signal.zpk(sys)

plt.show()