def mkpassword(length=16, chars=None, punctuation=None):
    if chars is None:
        chars = string.ascii_letters + string.digits
    data = [random.choice(chars) for _ in range(length)]
    if punctuation:
        data = data[:-punctuation]
        for _ in range(punctuation):
            data.append(random.choice(PUNCTUATION))
        random.shuffle(data)
    return ''.join(data)