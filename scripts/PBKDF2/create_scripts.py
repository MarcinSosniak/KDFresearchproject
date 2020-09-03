from os import listdir
from os.path import isfile, join
password_len = 3
hashes_file_path = 'PBKDF2_hashcat_hashes'

from_run_to_hashcat = '../../hashcat/hashcat-6.1.1'

from_run_to_hashes_path = '../../scripts/PBKDF2/PBKDF2_hashcat_hashes/'
preffix = 'hashcat -m 12100 -w 3 -a 3 --speed-only --potfile-disable --runtime=10 '
suffix = ''.join(['?a' for i in range(password_len)])

onlyfiles = [f for f in listdir(hashes_file_path) if isfile(join(hashes_file_path, f))]
with open('hash_cat_test_PBKDF2_SHA512_GPU.cmd','w') as f:
    f.write('cd '+ from_run_to_hashcat+'\n')
    for file in onlyfiles:
        f.write(preffix+'-D 2 '+from_run_to_hashes_path+file + ' '+ suffix + '\n')
        f.write('ECHO ' + ''.join(['=' for i in range(240)] )+'\n')

with open('hash_cat_test_PBKDF2_SHA512_CPU.cmd','w') as f:
    f.write('cd '+ from_run_to_hashcat+'\n')
    for file in onlyfiles:
        f.write(preffix+'-D 1 '+from_run_to_hashes_path+file + ' '+ suffix + '\n')
        f.write('ECHO ' + ''.join(['=' for i in range(240)] )+'\n')



