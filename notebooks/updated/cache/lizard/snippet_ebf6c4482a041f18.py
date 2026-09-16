def map_hubs_to_verticals():
    vertical_hub_map = {}
    for hub in HUBS_LIST:
        vertical_slug = hub['vertical']['slug']
        if vertical_slug not in vertical_hub_map:
            vertical_hub_map[vertical_slug] = {'name': hub['vertical'][
                'name'], 'hubs': [hub['slug']]}
        else:
            vertical_hub_map[vertical_slug]['hubs'].append(hub['slug'])
    return vertical_hub_map