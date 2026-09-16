def setOverlayRaw(self, ulOverlayHandle, pvBuffer, unWidth, unHeight, unDepth):
    fn = self.function_table.setOverlayRaw
    result = fn(ulOverlayHandle, pvBuffer, unWidth, unHeight, unDepth)
    return result