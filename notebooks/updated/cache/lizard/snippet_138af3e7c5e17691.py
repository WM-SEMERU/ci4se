def spi_ss_polarity(self, polarity):
    ret = api.py_aa_spi_master_ss_polarity(self.handle, polarity)
    _raise_error_if_negative(ret)