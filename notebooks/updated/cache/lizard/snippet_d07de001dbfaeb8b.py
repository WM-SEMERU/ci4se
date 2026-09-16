def isPairTag(self):
    if self.isComment() or self.isNonPairTag():
        return False
    if self.isEndTag():
        return True
    if self.isOpeningTag() and self.endtag:
        return True
    return False