def infographic_header_element(impact_function_name, feature, parent):
    _ = feature, parent
    string_format = infographic_header['string_format']
    if impact_function_name:
        header = string_format.format(impact_function_name=impact_function_name
            )
        return header.capitalize()
    return None