def regions():
    regions = []
    for region_name in RegionData:
        region = RegionInfo(name=region_name, endpoint=RegionData[
            region_name], connection_cls=CloudWatchConnection)
        regions.append(region)
    return regions