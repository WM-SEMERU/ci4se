def cirs_radec(self, epoch):
    r_au, dec, ra = to_polar(self.cirs_xyz(epoch).au)
    return Angle(radians=ra, preference='hours'), Angle(radians=dec, signed
        =True), Distance(r_au)