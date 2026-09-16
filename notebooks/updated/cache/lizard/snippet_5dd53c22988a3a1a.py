def validate_iops(iops):
    iops = integer(iops)
    if int(iops) == 0:
        return iops
    if int(iops) < 1000:
        raise ValueError('DBInstance Iops, if set, must be greater than 1000.')
    return iops