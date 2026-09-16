def hazards_for_layer(layer_geometry_key):
    result = []
    for hazard in hazard_all:
        if layer_geometry_key in hazard.get('allowed_geometries'):
            result.append(hazard)
    return sorted(result, key=lambda k: k['key'])