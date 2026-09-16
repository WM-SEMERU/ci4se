def rpy(self):
    x, y, z, w = self.x, self.y, self.z, self.w
    roll = math.atan2(2 * y * w - 2 * x * z, 1 - 2 * y * y - 2 * z * z)
    pitch = math.atan2(2 * x * w - 2 * y * z, 1 - 2 * x * x - 2 * z * z)
    yaw = math.asin(2 * x * y + 2 * z * w)
    return roll, pitch, yaw