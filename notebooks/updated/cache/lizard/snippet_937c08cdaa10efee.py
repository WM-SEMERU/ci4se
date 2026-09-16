def find_char_color(ansi_string, pos):
    result = list()
    position = 0
    for item in (i for i in RE_SPLIT.split(ansi_string) if i):
        if RE_SPLIT.match(item):
            result.append(item)
            if position is not None:
                position += len(item)
        elif position is not None:
            for char in item:
                if position == pos:
                    result.append(char)
                    position = None
                    break
                position += 1
    return ''.join(result)