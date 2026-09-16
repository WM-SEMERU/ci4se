def get_lib_name(self):
    import toml
    cfg = toml.load(self.path)
    name = cfg.get('lib', {}).get('name')
    if name is None:
        name = cfg.get('package', {}).get('name')
    if name is None:
        raise Exception(
            "Can not parse library name from Cargo.toml. Cargo.toml missing value for 'name' key in both the [package] section and the [lib] section"
            )
    name = re.sub('[./\\\\-]', '_', name)
    return name