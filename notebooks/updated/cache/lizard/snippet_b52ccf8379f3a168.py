def get_parsing_plan_log_str(obj_on_fs_to_parse, desired_type,
    log_only_last: bool, parser):
    loc = obj_on_fs_to_parse.get_pretty_location(blank_parent_part=
        log_only_last and not GLOBAL_CONFIG.full_paths_in_logs,
        compact_file_ext=True)
    return '{loc} -> {type} ------- using {parser}'.format(loc=loc, type=
        get_pretty_type_str(desired_type), parser=str(parser))