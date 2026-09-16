def __verify_server_version(self):
    if compare_versions('.'.join([_lib_major_version, _lib_minor_version]),
        self.product_version) > 0:
        logger.warning(
            'Client version {} connecting to server with newer minor release {}.'
            .format(_lib_full_version, self.product_version))
    if compare_versions(_lib_major_version, self.product_version) != 0:
        raise InvalidSwimlaneProductVersion(self, '{}.0'.format(
            _lib_major_version), '{}.0'.format(str(int(_lib_major_version) +
            1)))