def get_all_manifests(image, registry, insecure=False, dockercfg_path=None,
    versions=('v1', 'v2', 'v2_list')):
    digests = {}
    registry_session = RegistrySession(registry, insecure=insecure,
        dockercfg_path=dockercfg_path)
    for version in versions:
        response, _ = get_manifest(image, registry_session, version)
        if response:
            digests[version] = response
    return digests