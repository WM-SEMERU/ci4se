def align(text, character='=', replchar=None, pos=0):
    r
    line_list = text.splitlines()
    new_lines = align_lines(line_list, character, replchar, pos=pos)
    new_text = '\n'.join(new_lines)
    return new_text