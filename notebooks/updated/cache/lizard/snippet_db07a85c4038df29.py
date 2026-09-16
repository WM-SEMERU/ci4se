def sheetNames(book=None):
    if book:
        if not book.lower() in [x.lower() for x in bookNames()]:
            return False
    else:
        book = activeBook()
    if not book:
        return False
    poBook = PyOrigin.WorksheetPages(book)
    if not len(poBook):
        return None
    return [x.GetName() for x in poBook.Layers()]