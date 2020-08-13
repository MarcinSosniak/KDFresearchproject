import scrypt
h1 = scrypt.hash('password', 'random salt')
h2 = scrypt.hash('password', 'random salt')
scrypt.encrypt('a','b')
print(h1 == h2)