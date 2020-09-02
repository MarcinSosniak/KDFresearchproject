import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


Ns =[]
Rs =[]
GPU_s =[]
CPU_s =[]

with open('test_res.txt','r') as f:
    for line in f:
        if line.startswith('#'):
            continue
        line_s = line.split()
        Ns.append(int(line_s[0]))
        Rs.append(int(line_s[1]))
        GPU_s.append(int(line_s[2]))
        CPU_s.append(int(line_s[3]))


GPU_s = list(map(lambda x : 0 if x == 0 else np.log10(x),GPU_s))
CPU_s = list(map(lambda x : 0 if x ==0  else np.log10(x),CPU_s))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(Ns, Rs, GPU_s,marker ='^',label='GPU')
ax.scatter(Ns, Rs, CPU_s,marker='o',label='CPU')
ax.set_xlabel('N')
ax.set_ylabel('r')
ax.set_zlabel('Hashes [10^x / s]')
plt.title('Scrypt hashcat test GPU vs CPU')
# ax.sey_zlabal('time [s]')
plt.show()