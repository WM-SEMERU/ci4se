def iso13616Prepare(iban):
    A = ord('A')
    Z = ord('Z')
    iban = iban.upper()
    iban = iban[4:] + iban[:4]

    def charfunc(n):
        code = ord(n)
        if code >= A and code <= Z:
            return str(code - A + 10)
        else:
            return str(n)
    return ''.join(map(charfunc, list(iban)))