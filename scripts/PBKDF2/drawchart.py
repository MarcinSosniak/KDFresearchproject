import matplotlib.pyplot as plt

iterations = []
time_taken = []

with open('time_test_write_down','r') as f:
    for line in f:
        if line == '':
            continue
        line_s = line.split()
        iterations.append(int(line_s[0]))
        time_taken.append(float(line_s[1]))


plt.plot(iterations,time_taken)
plt.xlabel('iterations')
plt.ylabel('time [s]')
plt.title('PBKDF')
plt.show()