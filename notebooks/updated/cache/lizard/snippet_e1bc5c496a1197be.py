def _del_module(self, lpBaseOfDll):
    try:
        aModule = self.__moduleDict[lpBaseOfDll]
        del self.__moduleDict[lpBaseOfDll]
    except KeyError:
        aModule = None
        msg = 'Unknown base address %d' % HexDump.address(lpBaseOfDll)
        warnings.warn(msg, RuntimeWarning)
    if aModule:
        aModule.clear()