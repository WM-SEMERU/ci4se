def toFloat(value):
    if isinstance(value, str):
        value = value.upper()
        for char in ['N', 'S', 'E', 'W']:
            if char in value:
                value = SIGN[char] + value.replace(char, ':')
                break
    return angle.toFloat(value)