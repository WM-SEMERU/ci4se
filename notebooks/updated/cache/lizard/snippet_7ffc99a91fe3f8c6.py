def screenshot(self, viewID, filename):
    self._connection._sendStringCmd(tc.CMD_SET_GUI_VARIABLE, tc.
        VAR_SCREENSHOT, viewID, filename)