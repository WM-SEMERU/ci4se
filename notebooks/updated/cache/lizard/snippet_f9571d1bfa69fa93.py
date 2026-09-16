def rn(x, af, rate):
    taus, devs, errs, ns = at.adev(x, taus=[af * rate], data_type='phase',
        rate=rate)
    oadev_x = devs[0]
    mtaus, mdevs, errs, ns = at.mdev(x, taus=[af * rate], data_type='phase',
        rate=rate)
    mdev_x = mdevs[0]
    rn = pow(mdev_x / oadev_x, 2)
    return rn