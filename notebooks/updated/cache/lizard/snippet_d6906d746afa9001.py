def apply_timefactor(cls, values):
    if cls.TIME is True:
        return values * cls.get_timefactor()
    if cls.TIME is False:
        return values / cls.get_timefactor()
    return values