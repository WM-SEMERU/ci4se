def build_youngs_coppersmith_mfd(mfd):
    return Node('YoungsCoppersmithMFD', {'minMag': mfd.min_mag, 'bValue':
        mfd.b_val, 'characteristicMag': mfd.char_mag, 'characteristicRate':
        mfd.char_rate, 'binWidth': mfd.bin_width})