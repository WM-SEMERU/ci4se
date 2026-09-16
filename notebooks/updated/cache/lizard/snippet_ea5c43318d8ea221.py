def showMetadata(dat):
    _tmp = rm_values_fields(copy.deepcopy(dat))
    print(json.dumps(_tmp, indent=2))
    return