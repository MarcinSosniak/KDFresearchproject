from pbkdf2 import crypt
pwhash = crypt("secret")
if pwhash == crypt("secret", pwhash):
  print ("Password good")
else:
  print ("Invalid password")