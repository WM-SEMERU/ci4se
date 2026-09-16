def getThirdPartyLibCompilerFlags(self, libs):
    fmt = PrintingFormat.singleLine()
    if libs[0] == '--multiline':
        fmt = PrintingFormat.multiLine()
        libs = libs[1:]
    platformDefaults = True
    if libs[0] == '--nodefaults':
        platformDefaults = False
        libs = libs[1:]
    details = self.getThirdpartyLibs(libs, includePlatformDefaults=
        platformDefaults)
    return details.getCompilerFlags(self.getEngineRoot(), fmt)