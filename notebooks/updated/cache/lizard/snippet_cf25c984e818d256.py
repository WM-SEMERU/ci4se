def get_volumes(container_map, config, default_volume_paths, include_named):

    def _bind_volume_path(vol):
        if isinstance(vol, HostVolume):
            return resolve_value(vol.path)
        v_path = resolve_value(default_volume_paths.get(vol.name))
        if v_path:
            return v_path
        raise KeyError('No host-volume information found for alias {0}.'.
            format(vol))

    def _attached_volume_path(vol):
        if isinstance(vol, UsedVolume):
            return resolve_value(vol.path)
        v_path = resolve_value(default_volume_paths.get(vol.name))
        if v_path:
            return v_path
        raise KeyError('No volume information found for alias {0}.'.format(vol)
            )

    def _used_volume_path(vol):
        if isinstance(vol, UsedVolume):
            return resolve_value(vol.path)
        if container_map.use_attached_parent_name:
            return resolve_value(default_volume_paths.get(vol.name.
                partition('.')[2]))
        return resolve_value(default_volume_paths.get(vol.name))
    volumes = list(map(resolve_value, config.shares))
    volumes.extend(map(_bind_volume_path, config.binds))
    if include_named:
        volumes.extend(map(_attached_volume_path, config.attaches))
        volumes.extend(filter(None, map(_used_volume_path, config.uses)))
    return volumes