def check_earthquake_contour_preprocessor(impact_function):
    hazard_key = impact_function.hazard.keywords.get('hazard')
    is_earthquake = hazard_key == hazard_earthquake['key']
    if is_earthquake and is_raster_layer(impact_function.hazard):
        return True
    else:
        return False