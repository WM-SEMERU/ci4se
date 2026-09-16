def split_lines(lines):
    container = []
    new_list = []
    for line in lines:
        if '>>>' in line:
            container.append(new_list)
            new_list = []
        else:
            new_list.append(line)
    container.append(new_list)
    return container