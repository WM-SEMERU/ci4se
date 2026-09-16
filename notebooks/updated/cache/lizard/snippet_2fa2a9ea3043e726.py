def total_charge(self):
    charge = sum(self.data_points) / self.hz * 1000 / 3600
    return round(charge, self.sr)