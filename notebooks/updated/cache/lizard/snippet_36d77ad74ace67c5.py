def qteMakeAppletActive(self, applet: (QtmacsApplet, str)):
    if isinstance(applet, str):
        appletObj = self.qteGetAppletHandle(applet)
    else:
        appletObj = applet
    if appletObj not in self._qteAppletList:
        return False
    if self.qteIsMiniApplet(appletObj):
        if appletObj is not self._qteMiniApplet:
            self.qteLogger.warning('Wrong mini applet. Not activated.')
            print(appletObj)
            print(self._qteMiniApplet)
            return False
        if not appletObj.qteIsVisible():
            appletObj.show(True)
    elif not appletObj.qteIsVisible():
        self.qteReplaceAppletInLayout(appletObj)
    self._qteActiveApplet = appletObj
    return True