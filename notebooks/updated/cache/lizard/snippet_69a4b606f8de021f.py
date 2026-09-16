def get_line_number(doc, wrange):
    lineno = 1
    wrange.Select()
    wdFirstCharacterLineNumber = constants('wdFirstCharacterLineNumber')
    wdGoToLine = constants('wdGoToLine')
    wdGoToPrevious = constants('wdGoToPrevious')
    while True:
        curline = doc.Selection.Information(wdFirstCharacterLineNumber)
        doc.Selection.GoTo(wdGoToLine, wdGoToPrevious, Count=1, Name='')
        lineno += 1
        prevline = doc.Selection.Information(wdFirstCharacterLineNumber)
        if prevline == curline:
            break
    return lineno