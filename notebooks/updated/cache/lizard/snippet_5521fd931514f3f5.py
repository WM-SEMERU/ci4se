def disableGyro(self):
    logger.debug('Disabling gyro sensor')
    self.fifoSensorMask &= ~self.enableGyroMask
    self._gyroEnabled = False
    self._setSampleSizeBytes()