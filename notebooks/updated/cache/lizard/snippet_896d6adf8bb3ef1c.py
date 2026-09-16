def getControllerStateWithPose(self, eOrigin, unControllerDeviceIndex,
    unControllerStateSize=sizeof(VRControllerState_t)):
    fn = self.function_table.getControllerStateWithPose
    pControllerState = VRControllerState_t()
    pTrackedDevicePose = TrackedDevicePose_t()
    result = fn(eOrigin, unControllerDeviceIndex, byref(pControllerState),
        unControllerStateSize, byref(pTrackedDevicePose))
    return result, pControllerState, pTrackedDevicePose