def computeOverlayIntersection(self, ulOverlayHandle):
    fn = self.function_table.computeOverlayIntersection
    pParams = VROverlayIntersectionParams_t()
    pResults = VROverlayIntersectionResults_t()
    result = fn(ulOverlayHandle, byref(pParams), byref(pResults))
    return result, pParams, pResults