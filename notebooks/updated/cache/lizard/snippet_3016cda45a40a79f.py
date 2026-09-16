def xml_report_path(cls, resolution_cache_dir, resolve_hash_name, conf):
    return os.path.join(resolution_cache_dir, '{}-{}-{}.xml'.format(
        IvyUtils.INTERNAL_ORG_NAME, resolve_hash_name, conf))