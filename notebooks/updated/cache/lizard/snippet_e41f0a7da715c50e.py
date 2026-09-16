def get_polygon_pattern_rules(declarations, dirs):
    property_map = {'polygon-pattern-file': 'file', 'polygon-pattern-width':
        'width', 'polygon-pattern-height': 'height', 'polygon-pattern-type':
        'type', 'polygon-meta-output': 'meta-output', 'polygon-meta-writer':
        'meta-writer'}
    property_names = property_map.keys()
    rules = []
    for filter, values in filtered_property_declarations(declarations,
        property_names):
        (poly_pattern_file, poly_pattern_type, poly_pattern_width,
            poly_pattern_height) = (values.has_key('polygon-pattern-file') and
            post_process_symbolizer_image_file(str(values[
            'polygon-pattern-file'].value), dirs) or (None, None, None, None))
        poly_pattern_width = values.has_key('polygon-pattern-width'
            ) and values['polygon-pattern-width'].value or poly_pattern_width
        poly_pattern_height = values.has_key('polygon-pattern-height'
            ) and values['polygon-pattern-height'].value or poly_pattern_height
        symbolizer = poly_pattern_file and output.PolygonPatternSymbolizer(
            poly_pattern_file, poly_pattern_type, poly_pattern_width,
            poly_pattern_height)
        if symbolizer:
            rules.append(make_rule(filter, symbolizer))
    return rules