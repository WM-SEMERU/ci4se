def random_string(**kwargs):
    n = kwargs.get('length', 10)
    pool = kwargs.get('pool') or string.digits + string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(pool) for _ in range(n))