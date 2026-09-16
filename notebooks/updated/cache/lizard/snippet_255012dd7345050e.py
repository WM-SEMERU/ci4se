def get_list_url_tibiadata(cls, world, town, house_type: HouseType=
    HouseType.HOUSE):
    house_type = '%ss' % house_type.value
    return HOUSE_LIST_URL_TIBIADATA % (urllib.parse.quote(world), urllib.
        parse.quote(town), house_type)