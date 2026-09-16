def off(self):
    for device in self:
        if isinstance(device, (OutputDevice, CompositeOutputDevice)):
            device.off()