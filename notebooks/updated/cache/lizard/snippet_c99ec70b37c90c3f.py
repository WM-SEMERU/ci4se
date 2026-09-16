def AddAnalogShortIdMsecRecordNoStatus(site_service, tag, time_value, msec,
    value):
    szService = c_char_p(site_service.encode('utf-8'))
    szPointId = c_char_p(tag.encode('utf-8'))
    tTime = c_long(int(time_value))
    dValue = c_double(value)
    usMsec = c_ushort(msec)
    nRet = dnaserv_dll.DnaAddAnalogShortIdMsecRecordNoStatus(szService,
        szPointId, tTime, dValue, usMsec)
    return nRet