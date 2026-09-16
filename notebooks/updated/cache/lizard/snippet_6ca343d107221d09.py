def build_data_availability(datasets_json):
    data_availability = None
    if 'availability' in datasets_json and datasets_json.get('availability'):
        data_availability = datasets_json.get('availability')[0].get('text')
    return data_availability