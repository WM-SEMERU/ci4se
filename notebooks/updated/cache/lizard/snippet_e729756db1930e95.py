def _find_xinput(self):
    for dll in XINPUT_DLL_NAMES:
        try:
            self.xinput = getattr(ctypes.windll, dll)
        except OSError:
            pass
        else:
            self.xinput_dll = dll
            break
    else:
        warn('No xinput driver dll found, gamepads not supported.',
            RuntimeWarning)