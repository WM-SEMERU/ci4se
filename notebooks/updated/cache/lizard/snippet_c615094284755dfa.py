def _uniqueid(n=30):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase +
        string.ascii_lowercase) for _ in range(n))