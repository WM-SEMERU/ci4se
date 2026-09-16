def table(self, data, header=None):
    if header:
        x = PrettyTable(header)
    else:
        x = PrettyTable()
    for row in data:
        x.add_row(row)
    s = x.get_string(border=True)
    lines = s.split('\n')
    header_ = lines[:2]
    body = lines[2:]
    n_body = len(body)
    ruler = body[0]
    new_body = list()
    counter = 0
    for line in body:
        counter += 1
        new_body.append(line)
        if 2 <= counter and counter < n_body - 1:
            new_body.append(ruler)
    if header:
        return '\n'.join(header_ + new_body)
    else:
        return '\n'.join(new_body)