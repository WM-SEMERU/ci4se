def get_calculated_aes(aesthetics):
    calculated_aesthetics = []
    for name, value in aesthetics.items():
        if is_calculated_aes(value):
            calculated_aesthetics.append(name)
    return calculated_aesthetics