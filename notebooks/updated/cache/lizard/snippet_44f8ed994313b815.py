def getGyroData(self):
    x = self._readWord(self.REG_GYRO_XOUT_H)
    y = self._readWord(self.REG_GYRO_YOUT_H)
    z = self._readWord(self.REG_GYRO_ZOUT_H)
    gyro_scale_modifier = None
    gyro_range = self.readGyroRange()
    if gyro_range == self.GYRO_RANGE_250DEG:
        gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_250DEG
    elif gyro_range == self.GYRO_RANGE_500DEG:
        gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_500DEG
    elif gyro_range == self.GYRO_RANGE_1KDEG:
        gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_1KDEG
    elif gyro_range == self.GYRO_RANGE_2KDEG:
        gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_2KDEG
    else:
        print('ERROR: Unkown gyroscope range!')
        return False
    x = x / gyro_scale_modifier
    y = y / gyro_scale_modifier
    z = z / gyro_scale_modifier
    return {'x': x, 'y': y, 'z': z}