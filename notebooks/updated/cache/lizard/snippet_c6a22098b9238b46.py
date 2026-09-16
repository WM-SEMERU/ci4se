def crypt(password, cost=2):
    salt = _generate_salt(cost)
    hashed = pbkdf2.pbkdf2_hex(password, salt, cost * 500)
    return '$pbkdf2-256-1$' + str(cost) + '$' + salt.decode('utf-8'
        ) + '$' + hashed