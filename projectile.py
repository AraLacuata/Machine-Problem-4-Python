import math as math
import numpy as np
import matplotlib.pyplot as plt
ho = float(input('Initial height: '))
vo = float(input('Initial velocity: '))
th = float(input('Angle in degrees: '))
ax = float(input('x-component acceleration: '))
ay = float(input('y-component acceleration: '))
pr = float(input('Precision(Time Interval): '))

if ay >= 0:
    print('Positive or no vertical acceleration would result in no free fall. Aborting.')
    quit()
    
th = math.radians(th)
vox = vo*math.cos(th)
voy = vo*math.sin(th)

rt = [ay/2, voy, ho]
tm = max(np.roots(rt))
d = np.arange(0,tm,pr)
x = np.zeros(len(d)+1)
y = np.zeros(len(d)+1)

t = pr
x[0] = 0
y[0] = ho

n = np.arange(0,len(d)-1,1)
for i in n:
    xt = (ax*(t**2))/2 + vox*t
    yt = (ay*(t**2))/2 + voy*t + ho
    x[i+1] = xt
    y[i+1] = yt
    t=t+pr
    
x[len(d)] = (ax/2)*tm**2 + vox*tm
y[len(d)] = 0

plt.plot(x,y)
plt.xlabel('Distance')
plt.ylabel('Height')
plt.xlim(0,max(x)+1)
plt.ylim(0,max(y)+1)
plt.grid()
