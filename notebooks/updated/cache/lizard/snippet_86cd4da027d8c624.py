def __get_league_object():
    data = mlbgame.data.get_properties()
    return etree.parse(data).getroot().find('leagues').find('league')