def mod9710(iban):
    remainder = iban
    block = None
    while len(remainder) > 2:
        block = remainder[:9]
        remainder = str(int(block) % 97) + remainder[len(block):]
    return int(remainder) % 97