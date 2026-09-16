def parse_spec(spec, relative_to=None, subproject_roots=None):

    def normalize_absolute_refs(ref):
        return strip_prefix(ref, '//')
    subproject = longest_dir_prefix(relative_to, subproject_roots
        ) if subproject_roots else None

    def prefix_subproject(spec_path):
        if not subproject:
            return spec_path
        elif spec_path:
            return os.path.join(subproject, spec_path)
        else:
            return os.path.normpath(subproject)
    spec_parts = spec.rsplit(':', 1)
    if len(spec_parts) == 1:
        default_target_spec = spec_parts[0]
        spec_path = prefix_subproject(normalize_absolute_refs(
            default_target_spec))
        target_name = os.path.basename(spec_path)
    else:
        spec_path, target_name = spec_parts
        if not spec_path and relative_to:
            spec_path = fast_relpath(relative_to, subproject
                ) if subproject else relative_to
        spec_path = prefix_subproject(normalize_absolute_refs(spec_path))
    return spec_path, target_name