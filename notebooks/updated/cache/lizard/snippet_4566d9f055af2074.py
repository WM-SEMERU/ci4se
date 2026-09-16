def dosdate(dosdate, dostime):
    try:
        t = ord(dosdate[1]) << 8
        t |= ord(dosdate[0])
        day = t & 31
        month = (t & 480) >> 5
        year = (t & 65024) >> 9
        year += 1980
        t = ord(dostime[1]) << 8
        t |= ord(dostime[0])
        sec = t & 31
        sec *= 2
        minute = (t & 2016) >> 5
        hour = (t & 63488) >> 11
        return datetime(year, month, day, hour, minute, sec)
    except:
        return datetime.min