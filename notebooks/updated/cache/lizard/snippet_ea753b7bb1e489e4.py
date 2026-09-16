def standardizeMapName(mapName):
    newName = os.path.basename(mapName)
    newName = newName.split('.')[0]
    newName = newName.split('(')[0]
    newName = re.sub('[LT]E+$', '', newName)
    newName = re.sub('-', '', newName)
    newName = re.sub(' ', '', newName, flags=re.UNICODE)
    foreignName = newName
    if foreignName in c.mapNameTranslations:
        return c.mapNameTranslations[foreignName]
    return newName