def std_salt(length=16, lowercase=True):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if lowercase is True:
        alphabet += 'abcdefghijklmnopqrstuvwxyz'
    chars = []
    for i in range(length):
        chars.append(choice(alphabet))
    return ''.join(chars)