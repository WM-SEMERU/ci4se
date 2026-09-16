def joinCSVs(csvFilePaths, column, ouputFileName, separator=','):
    res = ''
    legend = []
    csvs = []
    for f in csvFilePaths:
        c = CSVFile()
        c.parse(f)
        csvs.append(c)
        legend.append(separator.join(c.legend.keys()))
    legend = separator.join(legend)
    lines = []
    for i in range(len(csvs[0])):
        val = csvs[0].get(i, column)
        line = separator.join(csvs[0][i])
        for c in csvs[1:]:
            for j in range(len(c)):
                if val == c.get(j, column):
                    line += separator + separator.join(c[j])
        lines.append(line)
    res = legend + '\n' + '\n'.join(lines)
    f = open(ouputFileName, 'w')
    f.write(res)
    f.flush()
    f.close()
    return res