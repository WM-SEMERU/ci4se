def cleanLines(source, lineSep=os.linesep):
    stripped = (line.strip(lineSep) for line in source)
    return (line for line in stripped if len(line) != 0)