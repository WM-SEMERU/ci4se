def get_query_parameters(config_parameters, date_time=datetime.datetime.now()):
    merged_parameters = Query.merge_parameters(config_parameters, date_time
        =date_time, macros=False, types_and_values=True)
    parsed_params = []
    for key, value in merged_parameters.items():
        parsed_params.append({'name': key, 'parameterType': {'type': value[
            'type']}, 'parameterValue': {'value': value['value']}})
    return parsed_params