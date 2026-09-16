def prepare_attached(self, action, a_name, **kwargs):
    client = action.client
    config_id = action.config_id
    policy = self._policy
    if action.container_map.use_attached_parent_name:
        v_alias = '{0.config_name}.{0.instance_name}'.format(config_id)
    else:
        v_alias = config_id.instance_name
    user = policy.volume_users[config_id.map_name][v_alias]
    permissions = policy.volume_permissions[config_id.map_name][v_alias]
    if not (self.prepare_local and hasattr(client, 'run_cmd')):
        return self._prepare_container(client, action, a_name, v_alias)
    if action.client_config.features['volumes']:
        volume_detail = client.inspect_volume(a_name)
        local_path = volume_detail['Mountpoint']
    else:
        instance_detail = client.inspect_container(a_name)
        volumes = get_instance_volumes(instance_detail, False)
        path = resolve_value(policy.default_volume_paths[config_id.map_name
            ][v_alias])
        local_path = volumes.get(path)
        if not local_path:
            raise ValueError(
                "Could not locate local path of volume alias '{0}' / path '{1}' in container {2}."
                .format(action.config_id.instance_name, path, a_name))
    return [client.run_cmd(cmd) for cmd in get_preparation_cmd(user,
        permissions, local_path)]