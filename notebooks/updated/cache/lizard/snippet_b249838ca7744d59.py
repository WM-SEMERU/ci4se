def Search(self, text, wholewords=0, titleonly=0):
    if text and text != '' and self.file:
        return extra.search(self.file, text, wholewords, titleonly)
    else:
        return None