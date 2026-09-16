def minutes_from_utc(self):
    offset = 0
    if self.__datetime is not None and self.__datetime.utcoffset() is not None:
        offset = self.__datetime.utcoffset().seconds / 60
        if self.__datetime.utcoffset().days == -1:
            offset = -(60 * 24 - offset)
    return int(offset)