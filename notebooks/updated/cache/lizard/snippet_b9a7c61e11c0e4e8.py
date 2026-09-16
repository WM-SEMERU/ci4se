def getScreenshotPropertyFilename(self, screenshotHandle, filenameType,
    pchFilename, cchFilename):
    fn = self.function_table.getScreenshotPropertyFilename
    pError = EVRScreenshotError()
    result = fn(screenshotHandle, filenameType, pchFilename, cchFilename,
        byref(pError))
    return result, pError