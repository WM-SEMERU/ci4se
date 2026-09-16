def add_expiration_postfix(expiration):
    if re.match('^[1-9][0-9]*$', expiration):
        return expiration + '.0a1'
    if re.match('^[1-9][0-9]*\\.0$', expiration):
        return expiration + 'a1'
    return expiration