def notify(self, msg='', title=None, delay=5000, image=''):
    if not msg:
        log.warning('Empty message for notification dialog')
    if title is None:
        title = self.addon.getAddonInfo('name')
    xbmc.executebuiltin('XBMC.Notification("%s", "%s", "%s", "%s")' % (msg,
        title, delay, image))