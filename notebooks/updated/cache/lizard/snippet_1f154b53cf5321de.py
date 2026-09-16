def get_map_config_ids(value, maps, default_map_name=None,
    default_instances=None):
    input_ids = InputConfigIdList(value, map_name=default_map_name,
        instances=default_instances)
    return list(expand_instances(expand_groups(input_ids, maps), maps))