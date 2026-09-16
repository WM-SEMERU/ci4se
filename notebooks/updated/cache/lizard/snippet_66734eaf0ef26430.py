def setSchema(self, viewID, schemeName):
    self._connection._sendStringCmd(tc.CMD_SET_GUI_VARIABLE, tc.
        VAR_VIEW_SCHEMA, viewID, schemeName)