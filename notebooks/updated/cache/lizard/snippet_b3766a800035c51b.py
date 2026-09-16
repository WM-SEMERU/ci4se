def blk_coverage_1d(blk, size):
    rem = size % blk
    maxpix = size - rem
    return maxpix, rem