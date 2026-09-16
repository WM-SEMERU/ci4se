def parse_csv_header(line):
    units = {}
    names = []
    for var in line.split(','):
        start = var.find('[')
        if start < 0:
            names.append(str(var))
            continue
        else:
            names.append(str(var[:start]))
        end = var.find(']', start)
        unitstr = var[start + 1:end]
        eq = unitstr.find('=')
        if eq >= 0:
            units[names[-1]] = unitstr[eq + 2:-1]
    return names, units