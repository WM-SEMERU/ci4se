def reducer_metro(self, metro, values):
    lookup = CachedLookup(precision=POI_GEOHASH_PRECISION)
    for i, value in enumerate(values):
        type_tag, lonlat, data = value
        if type_tag == 1:
            lookup.insert(i, dict(geometry=dict(type='Point', coordinates=
                project(lonlat)), properties=dict(tags=data)))
        else:
            if not lookup.data_store:
                return
            poi_names = []
            kwargs = dict(buffer_size=POI_DISTANCE, multiple=True)
            for poi in lookup.get(lonlat, **kwargs):
                has_tag = [(tag in poi['tags']) for tag in POI_TAGS]
                if any(has_tag) and 'name' in poi['tags']:
                    poi_names.append(poi['tags']['name'])
            for poi in set(poi_names):
                yield (metro, poi), 1