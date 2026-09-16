def isOpeningTag(self):
    if self.isTag() and not self.isComment() and not self.isEndTag(
        ) and not self.isNonPairTag():
        return True
    return False