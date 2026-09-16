def get_all_role_config_groups(resource_root, service_name, cluster_name=
    'default'):
    return call(resource_root.get, _get_role_config_groups_path(
        cluster_name, service_name), ApiRoleConfigGroup, True, api_version=3)