def datetimes(self):
    if self.timestep == 1:
        return tuple(dt.add_minute(30) for dt in self.
            direct_normal_irradiance.datetimes)
    else:
        return self.direct_normal_irradiance.datetimes