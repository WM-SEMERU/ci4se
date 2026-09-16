def clean_whitespace(string, compact=False):
    for a, b in (('\r\n', '\n'), ('\r', '\n'), ('\n\n', '\n'), ('\t', ' '),
        ('  ', ' ')):
        string = string.replace(a, b)
    if compact:
        for a, b in (('\n', ' '), ('[ ', '['), ('  ', ' '), ('  ', ' '), (
            '  ', ' ')):
            string = string.replace(a, b)
    return string.strip()