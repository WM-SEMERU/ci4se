def read(self, timeout=20.0):
    start = time()
    while len(self.rcv_data) == 0:
        sleep(0)
        if time() - start > timeout:
            raise DAPAccessIntf.DeviceError('Read timed out')
    return self.rcv_data.popleft()