def decompress(self, x, flag):
    x = self.field.value(x)
    ysquare = x ** 3 + self.a * x + self.b
    return self.point(x, ysquare.sqrt(flag))