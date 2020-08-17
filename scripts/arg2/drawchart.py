import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
MB = []
time_complexity = [] # time complexity
time_taken = []

with open('time_test_write_down','r') as f:
    for line in f:
        if line == '':
            continue
        line_s = line.split()
        MB.append(int(line_s[0]))
        time_complexity.append(int(line_s[1]))
        time_taken.append(float(line_s[2]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(MB,time_complexity,time_taken)
ax.set_xlabel('memory [MB]')
ax.set_ylabel('time complexity')
# ax.sey_zlabal('time [s]')
plt.show()