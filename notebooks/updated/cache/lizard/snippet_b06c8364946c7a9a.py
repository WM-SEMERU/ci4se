def i2c_slave_last_transmit_size(self):
    ret = api.py_aa_i2c_slave_write_stats(self.handle)
    _raise_error_if_negative(ret)
    return ret