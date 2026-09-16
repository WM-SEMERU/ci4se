def date_to_delorean(year, month, day):
    return Delorean(datetime=dt(year, month, day), timezone='UTC')