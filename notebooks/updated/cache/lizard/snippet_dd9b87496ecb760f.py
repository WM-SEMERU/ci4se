def api(feature='conditions', city='Portland', state='OR', key=None):
    features = (
        'alerts astronomy conditions currenthurricane forecast forecast10day geolookup history hourly hourly10day '
         + 'planner rawtide satellite tide webcams yesterday').split(' ')
    feature = util.fuzzy_get(features, feature)
    key = key or env.get('WUNDERGROUND', None, verbosity=-1) or env.get(
        'WUNDERGROUND_KEY', 'c45a86c2fc63f7d0', verbosity=-1)
    url = (
        'http://api.wunderground.com/api/{key}/{feature}/q/{state}/{city}.json'
        .format(key=key, feature=feature, state=state, city=city))
    return json.load(urllib.urlopen(url))