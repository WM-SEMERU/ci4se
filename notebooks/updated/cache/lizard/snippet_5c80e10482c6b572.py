def driverDebugRequest(self, unDeviceIndex, pchRequest, pchResponseBuffer,
    unResponseBufferSize):
    fn = self.function_table.driverDebugRequest
    result = fn(unDeviceIndex, pchRequest, pchResponseBuffer,
        unResponseBufferSize)
    return result