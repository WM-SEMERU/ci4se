def closeParagraph(self, mLastSection):
    result = ''
    if mLastSection != '':
        result = '</' + mLastSection + '>\n'
    return result