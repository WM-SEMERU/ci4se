def triggerHapticPulse(self, unControllerDeviceIndex, unAxisId,
    usDurationMicroSec):
    fn = self.function_table.triggerHapticPulse
    fn(unControllerDeviceIndex, unAxisId, usDurationMicroSec)