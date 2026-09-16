def echo(params, source, delay, strength):
    source = create_buffer(params, source)
    delay = create_buffer(params, delay)
    strength = create_buffer(params, strength)
    output = source[:]
    for i in range(params.length):
        d = int(i - delay[i])
        if 0 <= d < params.length:
            output[i] += source[d] * strength[i]
    return output