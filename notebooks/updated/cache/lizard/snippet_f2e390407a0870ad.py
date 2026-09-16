def get_vertical_and_horizontal(lines):
    vertical_lines = sorted([e for e in lines if e[1] == e[3]], key=lambda
        tup: (tup[1], tup[0]))
    horitontal_lines = sorted([e for e in lines if e[0] == e[2]])
    if len(vertical_lines) > 0:
        vertical_lines = merge_vertical_lines(vertical_lines)
    if len(horitontal_lines) > 0:
        horitontal_lines = merge_horizontal_lines(horitontal_lines)
    return vertical_lines, horitontal_lines