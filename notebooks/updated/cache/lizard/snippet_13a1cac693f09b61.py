def updateTargetState(self, newState):
    self._targetStateProvider.state = loadTargetState(newState, self.
        _targetStateProvider.state)
    for device in self.deviceController.getDevices():
        self.updateDeviceState(device.payload)