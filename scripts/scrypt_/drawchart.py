import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
MB = []
iterations = [] # time complexity
time_taken = []

with open('time_test_write_down','r') as f:
    for line in f:
        if line == '':
            continue
        line_s = line.split()
        MB.append(int(float(line_s[4])))
        iterations.append(int(line_s[0]))
        time_taken.append(float(line_s[2]))
        print('{} {} {}'.format(MB[-1],iterations[-1],time_taken[-1]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(MB, iterations, time_taken)
ax.set_xlabel('memory [MB]')
ax.set_ylabel('iterations')
ax.set_zlabel('time [s]')
plt.title('scrpyt')
# ax.sey_zlabal('time [s]')
plt.show()