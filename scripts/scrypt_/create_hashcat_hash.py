import scrypt
import base64
N = 1024
r = 8
p = 1

password = 'test'
salt = 'salt'



message_bytes = salt.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
salt_b64 = base64_bytes.decode('ascii')

print(salt_b64)

h1 = scrypt.hash('test', 'salt',p=1,N=1024,r=8,buflen=32)
# h2 = scrypt.hash('password', 'random salt',p=2)
# scrypt.encrypt('a','b')
# print(h1 == h2)
digest_b64= base64.b64encode(h1).decode('ascii')
print(digest_b64)

print('{}:{}:{}:{}:{}:{}'.format("SCRYPT",N,r,p,salt_b64,digest_b64))


