def copy(self):
    health = self.health, self.health_max
    r = self.r, self.r_max
    g = self.g, self.g_max
    b = self.b, self.b_max
    y = self.y, self.y_max
    x = self.x, self.x_max
    m = self.m, self.m_max
    h = self.h, self.h_max
    c = self.c, self.c_max
    return self.__class__(self.name, health, r, g, b, y, x, m, h, c)