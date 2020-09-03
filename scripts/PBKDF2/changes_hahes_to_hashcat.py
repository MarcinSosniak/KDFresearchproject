from os import listdir
from os.path import isfile, join
password_len = 3
hashes_file_path = 'PBKDF2_hashcat_hashes'


onlyfiles = [hashes_file_path+'/'+f for f in listdir(hashes_file_path) if isfile(join(hashes_file_path, f))]

for file_loc in onlyfiles:
    line =''
    with open(file_loc,'r') as f:
        line = f.readline()
    with open(file_loc,'w') as f:
        iters,hash = line.split(':')
        line = 'sha512:'+iters+':c2FsdA==:'+hash
        f.write(line)
