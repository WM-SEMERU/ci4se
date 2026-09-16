def _randomString():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for
        x in range(10))