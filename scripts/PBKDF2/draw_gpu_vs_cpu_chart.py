import matplotlib.pyplot as plt


iters = []
gpu = []
cpu = []
gpu_div_cpu = []

with open('test_res.txt','r') as f:
    for line in f:
        if line.startswith('#'):
            continue
        line_s = line.split()
        iters.append(int(line_s[0]))
        gpu.append(int(line_s[1]))
        cpu.append(int(line_s[2]))


gpu_div_cpu = list(map(lambda t : t[0]/t[1], list(zip(gpu,cpu))))
print(list(zip(iters,gpu_div_cpu)))
plt.plot(iters, gpu_div_cpu)
plt.xscale('log', basex=2)
plt.xlabel('iterations')
plt.ylabel('GPU/CPU hashes per second ratio')
plt.title('GPU vs CPU PBKDF2-HMAC-SHA512')
plt.show()