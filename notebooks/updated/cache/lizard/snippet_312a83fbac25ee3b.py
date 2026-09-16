def set_expire(self, y=2999, mon=12, d=28, h=23, min_=59, s=59):
    if type(y) is not int or type(mon) is not int or type(d
        ) is not int or type(h) is not int or type(min_) is not int or type(s
        ) is not int:
        raise KPError('Date variables must be integers')
    elif y > 9999 or y < 1 or mon > 12 or mon < 1 or d > 31 or d < 1 or h > 23 or h < 0 or min_ > 59 or min_ < 0 or s > 59 or s < 0:
        raise KPError('No legal date')
    elif (mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon ==
        10 or mon == 12) and d > 31 or (mon == 4 or mon == 6 or mon == 9 or
        mon == 11) and d > 30 or mon == 2 and d > 28:
        raise KPError("Given day doesn't exist in given month")
    else:
        self.expire = datetime(y, mon, d, h, min_, s)
        self.last_mod = datetime.now().replace(microsecond=0)
        return True