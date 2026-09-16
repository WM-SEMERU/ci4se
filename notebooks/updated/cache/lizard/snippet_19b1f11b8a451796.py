def unpackSample(self, rawData):
    length = len(rawData)
    unpacked = struct.unpack('>' + 'h' * (length // 2), memoryview(
        bytearray(rawData)).tobytes())
    mpu6050 = collections.OrderedDict()
    mpu6050[SAMPLE_TIME] = self._sampleIdx / self.fs
    sensorIdx = 0
    if self.isAccelerometerEnabled():
        mpu6050[ACCEL_X] = unpacked[sensorIdx] * self._accelerationFactor
        sensorIdx += 1
        mpu6050[ACCEL_Y] = unpacked[sensorIdx] * self._accelerationFactor
        sensorIdx += 1
        mpu6050[ACCEL_Z] = unpacked[sensorIdx] * self._accelerationFactor
        sensorIdx += 1
    if self.isTemperatureEnabled():
        mpu6050[TEMP] = unpacked[sensorIdx
            ] * self._temperatureGain + self._temperatureOffset
        sensorIdx += 1
    if self.isGyroEnabled():
        mpu6050[GYRO_X] = unpacked[sensorIdx] * self._gyroFactor
        sensorIdx += 1
        mpu6050[GYRO_Y] = unpacked[sensorIdx] * self._gyroFactor
        sensorIdx += 1
        mpu6050[GYRO_Z] = unpacked[sensorIdx] * self._gyroFactor
        sensorIdx += 1
    output = list(mpu6050.values())
    self._sampleIdx += 1
    return output