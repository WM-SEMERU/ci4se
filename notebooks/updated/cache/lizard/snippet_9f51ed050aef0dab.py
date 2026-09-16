def calculate_sunrise_sunset(locator, calc_date=datetime.utcnow()):
    morning_dawn = None
    sunrise = None
    evening_dawn = None
    sunset = None
    latitude, longitude = locator_to_latlong(locator)
    if type(calc_date) != datetime:
        raise ValueError
    sun = ephem.Sun()
    home = ephem.Observer()
    home.lat = str(latitude)
    home.long = str(longitude)
    home.date = calc_date
    sun.compute(home)
    try:
        nextrise = home.next_rising(sun)
        nextset = home.next_setting(sun)
        home.horizon = '-6'
        beg_twilight = home.next_rising(sun, use_center=True)
        end_twilight = home.next_setting(sun, use_center=True)
        morning_dawn = beg_twilight.datetime()
        sunrise = nextrise.datetime()
        evening_dawn = nextset.datetime()
        sunset = end_twilight.datetime()
    except ephem.AlwaysUpError as e:
        morning_dawn = None
        sunrise = None
        evening_dawn = None
        sunset = None
    except ephem.NeverUpError as e:
        morning_dawn = None
        sunrise = None
        evening_dawn = None
        sunset = None
    result = {}
    result['morning_dawn'] = morning_dawn
    result['sunrise'] = sunrise
    result['evening_dawn'] = evening_dawn
    result['sunset'] = sunset
    if morning_dawn:
        result['morning_dawn'] = morning_dawn.replace(tzinfo=UTC)
    if sunrise:
        result['sunrise'] = sunrise.replace(tzinfo=UTC)
    if evening_dawn:
        result['evening_dawn'] = evening_dawn.replace(tzinfo=UTC)
    if sunset:
        result['sunset'] = sunset.replace(tzinfo=UTC)
    return result