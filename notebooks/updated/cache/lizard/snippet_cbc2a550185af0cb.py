def dump_np_vars(self, store_format='csv', delimiter=','):
    ret = False
    if self.system.files.no_output is True:
        logger.debug('no_output is True, thus no TDS dump saved ')
        return True
    if self.write_lst() and self.write_np_dat(store_format=store_format,
        delimiter=delimiter):
        ret = True
    return ret