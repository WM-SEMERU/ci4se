def _extract_rsnap_isteps(rproffile):
    step_regex = re.compile('^\\*+step:\\s*(\\d+) ; time =\\s*(\\S+)')
    isteps = []
    rows_to_del = set()
    line = ' '
    with rproffile.open() as stream:
        while line[0] != '*':
            line = stream.readline()
        match = step_regex.match(line)
        istep = int(match.group(1))
        time = float(match.group(2))
        nlines = 0
        iline = 0
        for line in stream:
            if line[0] == '*':
                isteps.append((istep, time, nlines))
                match = step_regex.match(line)
                istep = int(match.group(1))
                time = float(match.group(2))
                nlines = 0
                nrows_to_del = 0
                while isteps and istep <= isteps[-1][0]:
                    nrows_to_del += isteps.pop()[-1]
                rows_to_del = rows_to_del.union(range(iline - nrows_to_del,
                    iline))
            else:
                nlines += 1
                iline += 1
        isteps.append((istep, time, nlines))
    return isteps, rows_to_del