def bits_to_dict(bits):
    cleaned_bits = [(bit[:-1] if bit.endswith(',') else bit) for bit in bits]
    options = dict(bit.split('=') for bit in cleaned_bits)
    for key in options:
        if options[key] == "'true'" or options[key] == "'false'":
            options[key] = options[key].title()
        options[key] = ast.literal_eval(options[key])
    return options