def parseString(txt, cip=True):
    if isinstance(txt, HTMLElement):
        return txt
    if len(txt) > 3 and txt[:3] == 'ï»¿':
        txt = txt[3:]
    if not cip:
        htmlelement.html_parser.SpecialDict = dict
    elif isinstance(htmlelement.html_parser.SpecialDict, dict):
        htmlelement.html_parser.SpecialDict = specialdict.SpecialDict
    container = HTMLElement()
    container.childs = _parseDOM([HTMLElement(x) for x in _raw_split(txt)])
    return container