def get_parameter_value_from_file_names(files, parameters=None, unique=
    False, sort=True):
    logging.debug('Get the parameter: ' + str(parameters) +
        ' values from the file names of ' + str(len(files)) + ' files')
    files_dict = collections.OrderedDict()
    if parameters is None:
        return files_dict
    if isinstance(parameters, basestring):
        parameters = parameters,
    search_string = '_'.join(parameters)
    for _ in parameters:
        search_string += '_(-?\\d+)'
    result = {}
    for one_file in files:
        parameter_values = re.findall(search_string, one_file)
        if parameter_values:
            if isinstance(parameter_values[0], tuple):
                parameter_values = list(reduce(lambda t1, t2: t1 + t2,
                    parameter_values))
            parameter_values = [[int(i)] for i in parameter_values]
            files_dict[one_file] = dict(zip(parameters, parameter_values))
            if unique:
                for key, value in files_dict.items():
                    if value not in result.values():
                        result[key] = value
            else:
                result[one_file] = files_dict[one_file]
    return collections.OrderedDict(sorted(result.iteritems(), key=
        itemgetter(1)) if sort else files_dict)