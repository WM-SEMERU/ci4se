def inject_code(self, payload, lpParameter=0):
    lpStartAddress = self.malloc(len(payload))
    try:
        self.write(lpStartAddress, payload)
        aThread = self.start_thread(lpStartAddress, lpParameter, bSuspended
            =False)
        aThread.pInjectedMemory = lpStartAddress
    except Exception:
        self.free(lpStartAddress)
        raise
    return aThread, lpStartAddress