def rc(self):
    m = Motif()
    m.pfm = [row[::-1] for row in self.pfm[::-1]]
    m.pwm = [row[::-1] for row in self.pwm[::-1]]
    m.id = self.id + '_revcomp'
    return m