def human_time(seconds):
    isec = int(seconds)
    s = isec % 60
    m = isec // 60 % 60
    h = isec // 60 // 60 % 24
    d = isec // 60 // 60 // 24 % 7
    w = isec // 60 // 60 // 24 // 7
    result = ''
    for t in [('W', w), ('D', d), ('h', h), ('m', m), ('s', s)]:
        if t[1]:
            result += str(t[1]) + t[0]
    return result