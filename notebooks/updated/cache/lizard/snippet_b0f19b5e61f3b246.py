def has_text_frame(self):
    dLbl = self._dLbl
    if dLbl is None:
        return False
    if dLbl.xpath('c:tx/c:rich'):
        return True
    return False