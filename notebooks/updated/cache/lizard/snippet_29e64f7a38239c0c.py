def qteUnbindAllFromApplet(self, applet: (QtmacsApplet, str)):
    if isinstance(applet, str):
        appletObj = self.qteGetAppletHandle(applet)
    else:
        appletObj = applet
    if appletObj is None:
        return
    appletObj._qteAdmin.keyMap = self.qteCopyGlobalKeyMap()
    for wid in appletObj._qteAdmin.widgetList:
        wid._qteAdmin.keyMap = self.qteCopyGlobalKeyMap()