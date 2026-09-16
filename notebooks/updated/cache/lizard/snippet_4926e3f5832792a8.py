def _fetchAllChildren(self):
    assert self.isSliceable, 'No underlying pandas object: self._ndFrame is None'
    childItems = []
    for subName in self._ndFrame.items:
        childItem = PandasDataFrameRti(self._ndFrame[subName], nodeName=
            subName, fileName=self.fileName, iconColor=self._iconColor,
            standAlone=False)
        childItems.append(childItem)
    if self._standAlone:
        childItems.append(self._createIndexRti(self._ndFrame.items, 'items'))
        childItems.append(self._createIndexRti(self._ndFrame.major_axis,
            'major_axis'))
        childItems.append(self._createIndexRti(self._ndFrame.minor_axis,
            'minor_axis'))
    return childItems