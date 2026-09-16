def get_instance_from_build_spec(cls, name, disk_path, build_spec, paths):
    instance = cls(name, disk_path, paths)
    instance.normalize_build_spec(build_spec)
    return instance