def getThirdPartyLibIncludeDirs(self, libs):
    platformDefaults = True
    if libs[0] == '--nodefaults':
        platformDefaults = False
        libs = libs[1:]
    details = self.getThirdpartyLibs(libs, includePlatformDefaults=
        platformDefaults)
    return details.getIncludeDirectories(self.getEngineRoot(), delimiter='\n')