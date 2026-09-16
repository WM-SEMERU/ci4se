def list_capability_definitions(service_instance=None):
    profile_manager = salt.utils.pbm.get_profile_manager(service_instance)
    ret_list = [_get_capability_definition_dict(c) for c in salt.utils.pbm.
        get_capability_definitions(profile_manager)]
    return ret_list