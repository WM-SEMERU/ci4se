def getArraysByName(elem, name):
    name = StripArrayName(name)
    return elem.getElements(lambda e: e.tagName == ligolw.Array.tagName and
        e.Name == name)