def qteSaveMacroData(self, data, widgetObj: QtGui.QWidget=None):
    if not hasattr(widgetObj, '_qteAdmin') and widgetObj is not None:
        msg = '<widgetObj> was probably not added with <qteAddWidget>'
        msg += ' method because it lacks the <_qteAdmin> attribute.'
        raise QtmacsOtherError(msg)
    if not widgetObj:
        widgetObj = self.qteWidget
    widgetObj._qteAdmin.macroData[self.qteMacroName()] = data