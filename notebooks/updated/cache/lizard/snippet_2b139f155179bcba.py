def current_bed_temp(self):
    try:
        bedtemps = self.intervals[0]['timeseries']['tempBedC']
        num_temps = len(bedtemps)
        if num_temps == 0:
            return None
        bedtemp = bedtemps[num_temps - 1][1]
    except KeyError:
        bedtemp = None
    return bedtemp