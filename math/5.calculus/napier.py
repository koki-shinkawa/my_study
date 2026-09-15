#5.6
import numpy as np
#print(np.e)

import matplotlib.pyplot as plt

#x = np.linspace(-2,2)
#y = np.exp(x) #ネイピア数のべき乗

#plt.plot(x,y)
#plt.xlabel("x",size=14)
#plt.ylabel("y",size=14)
#plt.grid()
#plt.show()

#自然対数　eを何乗したらxになるか
#print(np.log(np.e))

x = np.linspace(0.01,2)
y = np.log(x)

plt.plot(x,y)
plt.xlabel("x",size=14)
plt.ylabel("y",size=14)
plt.grid()
plt.show()


