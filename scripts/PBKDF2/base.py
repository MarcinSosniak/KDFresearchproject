from pbkdf2 import crypt
# pwhash = crypt("1234",iterations=100,salt='salt')
# print(pwhash)
# if pwhash == crypt("secret", pwhash):
#      print ("Password good")
# else:
#      print ("Invalid password")

password = '1234'
salt = 'salt'
iterations= 100

hash = crypt(password,iterations=iterations,salt=salt)
hash_s=hash.split('$')
print(hash_s)