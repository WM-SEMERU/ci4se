def get_source_attributes(source):
    attrs = {'id': source.source_id, 'name': source.name, 'tectonicRegion':
        source.tectonic_region_type}
    if isinstance(source, NonParametricSeismicSource):
        if source.data[0][0].weight is not None:
            weights = []
            for data in source.data:
                weights.append(data[0].weight)
            attrs['rup_weights'] = numpy.array(weights)
    print(attrs)
    return attrs