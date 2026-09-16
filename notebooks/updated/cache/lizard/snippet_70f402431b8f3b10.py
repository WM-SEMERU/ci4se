def getProjectionRaw(self, eEye):
    fn = self.function_table.getProjectionRaw
    pfLeft = c_float()
    pfRight = c_float()
    pfTop = c_float()
    pfBottom = c_float()
    fn(eEye, byref(pfLeft), byref(pfRight), byref(pfTop), byref(pfBottom))
    return pfLeft.value, pfRight.value, pfTop.value, pfBottom.value