import scrypt
import base64
N_list = [1 << i for i in range(10,20)]
r_list = [1,8,16,32]
p_list = [1]

password = '123'
salt = 'salt'


message_bytes = salt.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
salt_b64 = base64_bytes.decode('ascii')
# print(salt_b64)


for N in N_list:
    for r in r_list:
        for p in p_list:
            h1 = scrypt.hash(password, salt,p=p,N=N,r=r,buflen=32)
            # h2 = scrypt.hash('password', 'random salt',p=2)
            # scrypt.encrypt('a','b')
            # print(h1 == h2)
            digest_b64= base64.b64encode(h1).decode('ascii')
            # print(digest_b64)
            hashcat_stirng = '{}:{}:{}:{}:{}:{}'.format("SCRYPT",N,r,p,salt_b64,digest_b64)
            print(hashcat_stirng)

            with open('hash_cat_hashes/{}_{}_{}'.format(N,r,p),'w') as f:
                f.write(hashcat_stirng)


