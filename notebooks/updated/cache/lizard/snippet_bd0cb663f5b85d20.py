def gotoItem(self, path):
    if not path:
        return
    sections = nativestring(path).split('/')
    check = projex.text.underscore(sections[0])
    for i in range(self.uiContentsTREE.topLevelItemCount()):
        item = self.uiContentsTREE.topLevelItem(i)
        if check in (projex.text.underscore(item.text(0)), item.text(1)):
            item.gotoItem('/'.join(sections[1:]))
            break