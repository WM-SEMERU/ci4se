def alias(requestContext, seriesList, newName):
    try:
        seriesList.name = newName
    except AttributeError:
        for series in seriesList:
            series.name = newName
    return seriesList