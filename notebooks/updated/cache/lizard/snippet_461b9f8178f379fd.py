def getBoundsColor(self, nNumOutputColors, flCollisionBoundsFadeDistance):
    fn = self.function_table.getBoundsColor
    pOutputColorArray = HmdColor_t()
    pOutputCameraColor = HmdColor_t()
    fn(byref(pOutputColorArray), nNumOutputColors,
        flCollisionBoundsFadeDistance, byref(pOutputCameraColor))
    return pOutputColorArray, pOutputCameraColor