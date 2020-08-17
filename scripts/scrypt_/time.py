import numpy as np
import time
import scrypt

ITER_COUNTS  = [(1024*4)<<i for i in range(25)]
BLOCK_SIZES=[8*(2**i) for i in range(1)]
CALLS_FOR_TIME_MEASURMENT = 50
RETRIES_FOR_CALUCLATING_VARIANCE = 3
PASSWORD = "s3kr3tp4ssw0rd"

hash = None
print('iterations block mean stddev memomory_used[MB]')
with open('C:\AGH\s8\pracownia_projektowa\scripts\\scrypt_\\time_test_write_down','w') as f:
    for iters  in ITER_COUNTS:
        for blocks in BLOCK_SIZES:
            times = []
            for _ in range(RETRIES_FOR_CALUCLATING_VARIANCE):
                t_start = time.time()
                for _ in range(CALLS_FOR_TIME_MEASURMENT):
                    hash = scrypt.hash(PASSWORD, 'random salt',iters,blocks,1)
                t_end= time.time()
                times.append((t_end- t_start)/CALLS_FOR_TIME_MEASURMENT)
            line = '{} {} {} {} {}'.format(int(iters),blocks,np.mean(times),np.std(times),128*iters*blocks*1/(1024*1024))
            print(line)
            f.write(line+'\n')
            if np.mean(times) > 1:
                break
