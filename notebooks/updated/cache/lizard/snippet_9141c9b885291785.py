def getOverlayMouseScale(self, ulOverlayHandle):
    fn = self.function_table.getOverlayMouseScale
    pvecMouseScale = HmdVector2_t()
    result = fn(ulOverlayHandle, byref(pvecMouseScale))
    return result, pvecMouseScale