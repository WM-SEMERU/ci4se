def check_passwd(guess, passwd):
    m = sha1()
    salt = passwd[:salt_len * 2]
    m.update(unicode2bytes(guess) + unicode2bytes(salt))
    crypted_guess = bytes2unicode(salt) + m.hexdigest()
    return crypted_guess == bytes2unicode(passwd)