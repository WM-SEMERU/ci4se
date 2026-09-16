def qteUnbindKeyFromWidgetObject(self, keysequence, widgetObj: QtGui.QWidget):
    keysequence = QtmacsKeysequence(keysequence)
    if not hasattr(widgetObj, '_qteAdmin'):
        msg = '<widgetObj> was probably not added with <qteAddWidget>'
        msg += ' method because it lacks the <_qteAdmin> attribute.'
        raise QtmacsOtherError(msg)
    widgetObj._qteAdmin.keyMap.qteRemoveKey(keysequence)