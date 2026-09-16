def TriToBin(self, x, y, z):
    if z >= 0:
        if x + y + z == 0:
            return 0, 0
        else:
            Sum = x + y + z
            X = 100.0 * x / Sum
            Y = 100.0 * y / Sum
            Z = 100.0 * z / Sum
            if X + Y != 0:
                a = Z / 2.0 + (100.0 - Z) * Y / (Y + X)
            else:
                a = Z / 2.0
            b = Z / 2.0 * np.sqrt(3)
            return a, b
    else:
        z = abs(z)
        if x + y + z == 0:
            return 0, 0
        else:
            Sum = x + y + z
            X = 100.0 * x / Sum
            Y = 100.0 * y / Sum
            Z = 100.0 * z / Sum
            if X + Y != 0:
                a = Z / 2.0 + (100.0 - Z) * Y / (Y + X)
            else:
                a = Z / 2.0
            b = Z / 2.0 * np.sqrt(3)
            return a, -b