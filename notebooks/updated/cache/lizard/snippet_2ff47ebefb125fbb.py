def determine_final_freq(base, direction, modifier):
    result = 0
    if direction == '+':
        result = base + modifier
    elif direction == '-':
        result = base - modifier
    return result