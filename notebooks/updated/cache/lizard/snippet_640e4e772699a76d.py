def get_dict_definition(self, dict, get_list=False):
    list_def_candidate = []
    for definition_name in self.specification['definitions'].keys():
        if self.validate_definition(definition_name, dict):
            if not get_list:
                return definition_name
            list_def_candidate.append(definition_name)
    if get_list:
        return list_def_candidate
    return None