def clearOverlayTexture(self, ulOverlayHandle):
    fn = self.function_table.clearOverlayTexture
    result = fn(ulOverlayHandle)
    return result