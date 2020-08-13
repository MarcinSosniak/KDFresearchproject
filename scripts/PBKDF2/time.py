import numpy as np
import time
from pbkdf2 import crypt

PASSWORD = "s3kr3tp4ssw0rd"
ITERATIONS = [1024<<i for i in range(100)]
CALLS_FOR_TIME_MEASURMENT = 100
RETRIES_FOR_CALUCLATING_VARIANCE = 5

print('iterations mean stddev')
with open('C:\AGH\s8\pracownia_projektowa\scripts\\PBKDF2\\time_test_write_down','w') as f:
    for iters in ITERATIONS:
        times = []
        for _ in range(RETRIES_FOR_CALUCLATING_VARIANCE):
            t_start = time.time()
            for _ in range(CALLS_FOR_TIME_MEASURMENT):
                hash = crypt(PASSWORD,iterations=iters)
            t_end = time.time()
            times.append((t_end - t_start) / CALLS_FOR_TIME_MEASURMENT)
        line = '{} {} {}'.format(iters, np.mean(times), np.std(times))
        print(line)
        f.write(line + '\n')
        if np.mean(times) > 1:
            break
