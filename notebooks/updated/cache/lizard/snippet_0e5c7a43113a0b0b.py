def getPageType(name, number=False):
    if not name in pageNames():
        return None
    pageType = PyOrigin.Pages(name).GetType()
    if number:
        return str(pageType)
    if pageType == 1:
        return 'matrix'
    if pageType == 2:
        return 'book'
    if pageType == 3:
        return 'graph'
    if pageType == 4:
        return 'layout'
    if pageType == 5:
        return 'notes'