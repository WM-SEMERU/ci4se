def interp_data(self, latitude, longitude, utc_time, param):
    nctime = self.data['time']
    ilat, ilon = self.get_nearest_indices(latitude, longitude)
    before = netCDF4.date2index(utc_time, nctime, select='before')
    fbefore = self.data[param][before, ilat, ilon]
    fafter = self.data[param][before + 1, ilat, ilon]
    dt_num = netCDF4.date2num(utc_time, nctime.units)
    time_ratio = (dt_num - nctime[before]) / self.delta_time
    return fbefore + (fafter - fbefore) * time_ratio