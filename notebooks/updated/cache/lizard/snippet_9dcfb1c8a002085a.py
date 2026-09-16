def get_manifest_list_only_expectation(self):
    if not self.workflow.postbuild_results.get(PLUGIN_GROUP_MANIFESTS_KEY):
        self.log.debug(
            'Cannot check if only manifest list digest should be returned because group manifests plugin did not run'
            )
        return False
    platforms = get_platforms(self.workflow)
    if not platforms:
        self.log.debug(
            'Cannot check if only manifest list digest should be returned because we have no platforms list'
            )
        return False
    try:
        platform_to_goarch = get_platform_to_goarch_mapping(self.workflow)
    except KeyError:
        self.log.debug(
            'Cannot check if only manifest list digest should be returned because there are no platform descriptors'
            )
        return False
    for plat in platforms:
        if platform_to_goarch[plat] == 'amd64':
            self.log.debug('amd64 was built, all media types available')
            return False
    self.log.debug(
        'amd64 was not built, only manifest list digest is available')
    return True