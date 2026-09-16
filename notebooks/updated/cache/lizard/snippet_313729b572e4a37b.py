def get_isbn13_checksum(isbn):
    multipliers = map(lambda x: int(x), list('13' * 6))
    rest = sum([(i * x) for i, x in zip(multipliers, isbn)]) % 10
    if rest == 0:
        return rest
    return 10 - rest