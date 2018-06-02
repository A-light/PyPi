import matplotlib.pyplot as plt 
import numpy as np
def frange(start,stop,step=1.0):
	while start < stop:
		yield start
		start+=step

#X=list(frange(0,11,0.1))
#X=[v*0.05 for v in range(0,int(1/0.05))];
X=np.arange(0.,1.,0.01)
print(X)
y=[x*x for x in X]
print(y)
plt.plot(X,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=x^2')
plt.show()
