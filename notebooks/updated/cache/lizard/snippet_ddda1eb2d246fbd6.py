def parseStorage(storageData):
    if storageData == 'EBS only':
        return [0, 0]
    else:
        specs = storageData.strip().split()
        if isNumber(specs[0]) and specs[1] == 'x' and isNumber(specs[2]):
            return float(specs[0].replace(',', '')), float(specs[2].replace
                (',', ''))
        else:
            raise RuntimeError(
                'EC2 JSON format has likely changed.  Error parsing disk specs.'
                )