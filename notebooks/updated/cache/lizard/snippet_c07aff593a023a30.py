def get_context(self, context):
    i = 0
    while i < len(self.tagList):
        tag = self.tagList[i]
        if tag.tagClass == Tag.applicationTagClass:
            pass
        elif tag.tagClass == Tag.contextTagClass:
            if tag.tagNumber == context:
                return tag
        elif tag.tagClass == Tag.openingTagClass:
            keeper = tag.tagNumber == context
            rslt = []
            i += 1
            lvl = 0
            while i < len(self.tagList):
                tag = self.tagList[i]
                if tag.tagClass == Tag.openingTagClass:
                    lvl += 1
                elif tag.tagClass == Tag.closingTagClass:
                    lvl -= 1
                    if lvl < 0:
                        break
                rslt.append(tag)
                i += 1
            if lvl >= 0:
                raise InvalidTag('mismatched open/close tags')
            if keeper:
                return TagList(rslt)
        else:
            raise InvalidTag('unexpected tag')
        i += 1
    return None