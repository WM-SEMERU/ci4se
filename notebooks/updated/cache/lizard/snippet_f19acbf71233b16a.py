def ComputeGMST(GPSTime):
    D = np.round((GPSTime - EpochJ2000_0_UTC) / secPerDay) - 0.5
    T = D / 36525
    GMST0 = 6.697374558 + 2400.051336 * T + 2.5862e-05 * T * T
    GMST0 = np.mod(GMST0, 24)
    UTCSec = (GPSTime - EpochJ2000_0_UTC - secPerDay / 2 -
        LeapSeconds_2012_EpochJ2000)
    UTCHr = np.mod(UTCSec / 3600, 24)
    GMST = GMST0 + UTCHr * 1.002737909
    GMST = np.mod(GMST, 24)
    GMST *= 15.0 * (np.pi / 180.0)
    return GMST