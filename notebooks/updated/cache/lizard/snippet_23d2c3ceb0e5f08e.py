def qteUnbindKeyApplet(self, applet: (QtmacsApplet, str), keysequence):
    if isinstance(applet, str):
        appletObj = self.qteGetAppletHandle(applet)
    else:
        appletObj = applet
    if appletObj is None:
        return
    keysequence = QtmacsKeysequence(keysequence)
    appletObj._qteAdmin.keyMap.qteRemoveKey(keysequence)
    for wid in appletObj._qteAdmin.widgetList:
        self.qteUnbindKeyFromWidgetObject(keysequence, wid)