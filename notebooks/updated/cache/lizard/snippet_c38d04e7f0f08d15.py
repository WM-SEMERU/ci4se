def _from_dict_record(data):
    return [Schema._get_field_entry(name, value) for name, value in list(
        data.items())]