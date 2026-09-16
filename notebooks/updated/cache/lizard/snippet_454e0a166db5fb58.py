def qteBindKeyWidget(self, keysequence, macroName: str, widgetObj: QtGui.
    QWidget):
    keysequence = QtmacsKeysequence(keysequence)
    if not hasattr(widgetObj, '_qteAdmin'):
        msg = '<widgetObj> was probably not added with <qteAddWidget>'
        msg += ' method because it lacks the <_qteAdmin> attribute.'
        raise QtmacsOtherError(msg)
    if not self.qteIsMacroRegistered(macroName):
        msg = 'Cannot bind key to unknown macro <b>{}</b>.'.format(macroName)
        self.qteLogger.error(msg, stack_info=True)
        return False
    try:
        widgetObj._qteAdmin.keyMap.qteInsertKey(keysequence, macroName)
    except AttributeError:
        msg = 'Received an invalid macro object.'
        self.qteLogger.error(msg, stack_info=True)
        return False
    return True