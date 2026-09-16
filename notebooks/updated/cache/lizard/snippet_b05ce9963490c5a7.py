def save_twi(self, rootpath, raw=False, as_int=True):
    self.twi = np.ma.masked_array(self.twi, mask=self.twi <= 0, fill_value=
        -9999)
    self.twi[self.flats] = 0
    self.twi.mask[self.flats] = True
    self.save_array(self.twi, None, 'twi', rootpath, raw, as_int=as_int)