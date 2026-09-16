def getOverlayFlag(self, ulOverlayHandle, eOverlayFlag):
    fn = self.function_table.getOverlayFlag
    pbEnabled = openvr_bool()
    result = fn(ulOverlayHandle, eOverlayFlag, byref(pbEnabled))
    return result, pbEnabled