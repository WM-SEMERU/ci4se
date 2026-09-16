def from_bank_code(cls, country_code, bank_code):
    try:
        return cls(registry.get('bank_code')[country_code, bank_code]['bic'])
    except KeyError:
        raise ValueError('Invalid bank code {!r} for country {!r}'.format(
            bank_code, country_code))