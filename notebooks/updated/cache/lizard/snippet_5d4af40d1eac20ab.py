def freeze(plugins_directory):
    package_versions = []
    for plugin_path_i in plugins_directory.dirs():
        try:
            plugin_metadata = yaml.load(plugin_path_i.joinpath(
                'properties.yml').bytes())
            if plugin_path_i.name != plugin_metadata['package_name']:
                continue
            package_versions.append((plugin_metadata['package_name'],
                plugin_metadata['version']))
        except:
            continue
    return [('%s==%s' % v) for v in package_versions]