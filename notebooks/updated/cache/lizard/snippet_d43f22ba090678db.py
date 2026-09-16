def read_cz_lsm_info(fd, byte_order, dtype, count):
    result = numpy.rec.fromfile(fd, CZ_LSM_INFO, 1, byteorder=byte_order)[0]
    {(50350412): '1.3', (67127628): '2.0'}[result.magic_number]
    return result