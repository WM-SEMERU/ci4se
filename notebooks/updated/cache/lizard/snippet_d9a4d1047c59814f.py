def setOverlayWidthInMeters(self, ulOverlayHandle, fWidthInMeters):
    fn = self.function_table.setOverlayWidthInMeters
    result = fn(ulOverlayHandle, fWidthInMeters)
    return result