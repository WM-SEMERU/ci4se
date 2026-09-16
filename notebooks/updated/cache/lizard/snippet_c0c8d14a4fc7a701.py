def pressKeyCode(self, keycode, metaState=0):
    if self.uiAutomatorHelper:
        if DEBUG_UI_AUTOMATOR_HELPER:
            print >> sys.stderr, 'pressKeyCode(%d, %d)' % (keycode, metaState)
        self.uiAutomatorHelper.pressKeyCode(keycode, metaState)
    else:
        warnings.warn(
            'pressKeyCode only implemented using UiAutomatorHelper.  Use AdbClient.type() instead'
            )