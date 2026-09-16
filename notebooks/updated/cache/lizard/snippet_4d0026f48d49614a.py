def sdk_version(self):
    if self.__sdk == 0:
        try:
            self.__sdk = int(self.adb.cmd('shell', 'getprop',
                'ro.build.version.sdk').communicate()[0].decode('utf-8').
                strip())
        except:
            pass
    return self.__sdk