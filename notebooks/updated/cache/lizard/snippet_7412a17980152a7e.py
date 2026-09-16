def as_cep(numero):
    _numero = digitos(numero)
    if is_cep(_numero):
        return '{}-{}'.format(_numero[:5], _numero[5:])
    return numero