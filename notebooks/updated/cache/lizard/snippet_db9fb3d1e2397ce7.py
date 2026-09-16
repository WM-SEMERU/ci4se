def in_words(amount, gender=None):
    try:
        res = numeral.in_words(amount, getattr(numeral, str(gender), None))
    except Exception as err:
        res = default_value % {'error': err, 'value': str(amount)}
    return res