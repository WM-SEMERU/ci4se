def return_dat(self, chan, begsam, endsam):
    interval = endsam - begsam
    dat = empty((len(chan), interval))
    for i, chan in enumerate(chan):
        k = 0
        with open(self.chan_files[chan], 'rt') as f:
            f.readline()
            for j, datum in enumerate(f):
                if begsam <= j + 1 < endsam:
                    dat[i, k] = float64(datum)
                    k += 1
                    if k == interval:
                        break
    phys_range = self.phys_max - self.phys_min
    dig_range = self.dig_max - self.dig_min
    gain = phys_range / dig_range
    dat *= gain
    return dat