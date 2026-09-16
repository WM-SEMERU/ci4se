def select_functions(expr):
    body = Group(expr)
    return Group(function('timestamp', body, caseless=True) | function('ts',
        body, caseless=True) | function('utctimestamp', body, caseless=True
        ) | function('utcts', body, caseless=True) | function('now',
        caseless=True) | function('utcnow', caseless=True)).setResultsName(
        'function')