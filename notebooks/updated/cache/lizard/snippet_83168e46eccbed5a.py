def _cut_line(line):
    if re.search('([\t\n\r]+|[\x0b\x0c ]{3,})+', line):
        tmp = re.split('([\t\n\r]+|[\x0b\x0c ]{3,})+', line, 1)
    else:
        tmp = re.split('[' + string.whitespace + ']+', line, 1)
    res = [elt.strip() for elt in tmp if elt.strip() != '']
    return res