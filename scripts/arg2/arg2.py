from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("s3kr3tp4ssw0rd")
print(hash)  # doctest: +SKIP

#'$argon2id$v=19$m=102400,t=2,p=8$tSm+JOWigOgPZx/g44K5fQ$WDyus6py50bVFIPkjA28lQ'
print(ph.verify(hash, "s3kr3tp4ssw0rd"))
print(ph.check_needs_rehash(hash))
print(ph.verify(hash, "t0t411ywr0ng"))