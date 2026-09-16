def _decodeTimestamp(byteIter):
    dateStr = decodeSemiOctets(byteIter, 7)
    timeZoneStr = dateStr[-2:]
    return datetime.strptime(dateStr[:-2], '%y%m%d%H%M%S').replace(tzinfo=
        SmsPduTzInfo(timeZoneStr))