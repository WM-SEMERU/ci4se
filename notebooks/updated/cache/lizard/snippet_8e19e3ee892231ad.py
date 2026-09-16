def forecast(place, series=True):
    lat, lon = place
    url = (
        'http://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?' +
        'whichClient=NDFDgen&' + 'lat=%s&lon=%s&' % (lat, lon) +
        'Unit=e&temp=temp&wspd=wspd&sky=sky&wx=wx&rh=rh&' +
        'product=time-series&Submit=Submit')
    logger.debug(url)
    res = urllib2.urlopen(url).read()
    root = ET.fromstring(res)
    time_series = [i.text for i in root.findall('./data/time-layout')[0].
        iterfind('start-valid-time')]
    logger.debug(res)
    wind_speed = [(eval(i.text) * 1.15) for i in root.findall(
        './data/parameters/wind-speed')[0].iterfind('value')]
    cloud_cover = [(eval(i.text) / 100.0) for i in root.findall(
        './data/parameters/cloud-amount')[0].iterfind('value')]
    temperature = [eval(i.text) for i in root.findall(
        './data/parameters/temperature')[0].iterfind('value')]
    if not series:
        return {'cloudCover': cloud_cover[0], 'temperature': temperature[0],
            'windSpeed': wind_speed[0], 'start-valid-time': time_series[0]}
    else:
        return {'cloudCover': cloud_cover, 'temperature': temperature,
            'windSpeed': wind_speed, 'start-valid-time': time_series}