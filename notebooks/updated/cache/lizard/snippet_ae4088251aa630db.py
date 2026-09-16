def _importDinosaurTsv(filelocation):
    with io.open(filelocation, 'r', encoding='utf-8') as openFile:
        lines = openFile.readlines()
        headerDict = dict([[y, x] for x, y in enumerate(lines[0].strip().
            split('\t'))])
        featureDict = dict()
        for linePos, line in enumerate(lines[1:]):
            featureId = str(linePos)
            fields = line.strip().split('\t')
            entryDict = dict()
            for headerName, headerPos in viewitems(headerDict):
                entryDict[headerName] = float(fields[headerPos])
                if headerName in ['rtApex', 'rtEnd', 'rtStart', 'fwhm']:
                    entryDict[headerName] *= 60
                elif headerName in ['charge', 'intensitySum', 'nIsotopes',
                    'nScans', 'intensityApex']:
                    entryDict[headerName] = int(entryDict[headerName])
            featureDict[featureId] = entryDict
    return featureDict