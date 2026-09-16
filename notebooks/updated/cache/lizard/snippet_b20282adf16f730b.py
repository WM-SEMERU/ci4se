def sil(msg, version):
    tc = typecode(msg)
    if tc not in [29, 31]:
        raise RuntimeError(
            '%s: Not a target state and status messag,                            or operation status message, expecting TC = 29 or 31'
             % msg)
    msgbin = common.hex2bin(msg)
    if tc == 29:
        SIL = common.bin2int(msgbin[76:78])
    elif tc == 31:
        SIL = common.bin2int(msgbin[82:84])
    try:
        PE_RCu = uncertainty.SIL[SIL]['PE_RCu']
        PE_VPL = uncertainty.SIL[SIL]['PE_VPL']
    except KeyError:
        PE_RCu, PE_VPL = uncertainty.NA, uncertainty.NA
    base = 'unknown'
    if version == 2:
        if tc == 29:
            SIL_SUP = common.bin2int(msgbin[39])
        elif tc == 31:
            SIL_SUP = common.bin2int(msgbin[86])
        if SIL_SUP == 0:
            base = 'hour'
        elif SIL_SUP == 1:
            base = 'sample'
    return PE_RCu, PE_VPL, base