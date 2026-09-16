def decode_name(s):
    return re.sub('&#(\\d+);', lambda x: chr(int(x.group(1))), s)