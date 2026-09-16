def get_list_url(cls, world, town, house_type: HouseType=HouseType.HOUSE):
    house_type = '%ss' % house_type.value
    return HOUSE_LIST_URL % (urllib.parse.quote(world), urllib.parse.quote(
        town), house_type)