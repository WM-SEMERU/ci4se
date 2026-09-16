def __get_path_parameters(self, path):
    path_parameters_by_segment = {}
    for format_var_name in re.findall(_PATH_VARIABLE_PATTERN, path):
        first_segment = format_var_name.split('.', 1)[0]
        matches = path_parameters_by_segment.setdefault(first_segment, [])
        matches.append(format_var_name)
    return path_parameters_by_segment