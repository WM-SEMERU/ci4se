def _ConvertListToObject(cls, json_list):
    list_value = []
    for json_list_element in json_list:
        if isinstance(json_list_element, dict):
            list_value.append(cls._ConvertDictToObject(json_list_element))
        elif isinstance(json_list_element, list):
            list_value.append(cls._ConvertListToObject(json_list_element))
        else:
            list_value.append(json_list_element)
    return list_value