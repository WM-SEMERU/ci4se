def detect(self, fstring, fname=None):
    if fname is not None and '.' in fname:
        extension = fname.rsplit('.', 1)[1]
        if extension in {'pdf', 'html', 'xml'}:
            return False
    return True