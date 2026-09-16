def cardChunk(key, chunk):
    for line in chunk:
        values = []
        sline = line.strip().split()
        for idx in range(1, len(sline)):
            values.append(sline[idx])
    return {'card': sline[0], 'values': values}