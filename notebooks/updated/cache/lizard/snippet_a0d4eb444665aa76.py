def move_roles_to_base_role_config_group(resource_root, service_name,
    role_names, cluster_name='default'):
    return call(resource_root.put, _get_role_config_groups_path(
        cluster_name, service_name) + '/roles', ApiRole, True, data=
        role_names, api_version=3)