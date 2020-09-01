import scrypt
h1 = scrypt.hash('password', 'random salt',p=2)
h2 = scrypt.hash('password', 'random salt',p=2)
scrypt.encrypt('a','b')
print(h1 == h2)