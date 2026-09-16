def predict_pRF_radius(eccentricity, visual_area='V1', source='Wandell2015'):
    visual_area = visual_area.lower()
    if pimms.is_str(source):
        source = source.lower()
        if source not in pRF_data:
            raise ValueError(
                'Given source (%s) not found in pRF-size database' % source)
        dat = pRF_data[source]
        dat = dat[visual_area]
    else:
        dat = {'m': source[0], 'b': source[1]}
    return dat['m'] * eccentricity + dat['b']