def getOverlayTextureSize(self, ulOverlayHandle):
    fn = self.function_table.getOverlayTextureSize
    pWidth = c_uint32()
    pHeight = c_uint32()
    result = fn(ulOverlayHandle, byref(pWidth), byref(pHeight))
    return result, pWidth.value, pHeight.value