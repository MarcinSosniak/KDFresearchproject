from argon2 import PasswordHasher
import numpy as np
import time

time_coplexity = [i for i in range(1,15)]
MEMORY_COSTS_IN_MB=[128,512,1024,2048]
CALLS_FOR_TIME_MEASURMENT = 50
RETRIES_FOR_CALUCLATING_VARIANCE = 3
PASSWORD = "s3kr3tp4ssw0rd"
memory_costs = list(map(lambda x: 1024*x,MEMORY_COSTS_IN_MB))
hash = None
print('memory[MB] time_cost_level mean stddev')
with open('C:\AGH\s8\pracownia_projektowa\scripts\\arg2\\time_test_write_down','w') as f:
    for mem_cost in memory_costs:
        for time_cost in time_coplexity:
            ph = PasswordHasher(time_cost=time_cost,memory_cost=mem_cost)
            times = []
            for _ in range(RETRIES_FOR_CALUCLATING_VARIANCE):
                t_start = time.time()
                for _ in range(CALLS_FOR_TIME_MEASURMENT):
                    hash = ph.hash(PASSWORD)
                t_end= time.time()
                times.append((t_end- t_start)/CALLS_FOR_TIME_MEASURMENT)
            line = '{} {} {} {}'.format(int(mem_cost/1024),time_cost,np.mean(times),np.std(times))
            print(line)
            f.write(line+'\n')
            if np.mean(times) > 2:
                break
