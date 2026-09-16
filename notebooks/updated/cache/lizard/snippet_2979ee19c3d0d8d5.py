def to_euler_deg(self, euler_vec3):
    sqw = self.w * self.w
    sqx = self.x * self.x
    sqy = self.y * self.y
    sqz = self.z * self.z
    euler_vec3.z = math.atan2(2.0 * (self.x * self.y + self.z * self.w), 
        sqx - sqy - sqz + sqw) * (180.0 / math.pi)
    euler_vec3.x = math.atan2(2.0 * (self.y * self.z + self.x * self.w), -
        sqx - sqy + sqz + sqw) * (180.0 / math.pi)
    euler_vec3.y = math.asin(-2.0 * (self.x * self.z - self.y * self.w)) * (
        180.0 / math.pi)
    return euler_vec3