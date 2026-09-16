def flags(cmd, data):
    if cmd.lower() == 'a':
        indices = range(len(data))
        return [index for index in indices if index % 7 in [3, 4]]
    return []