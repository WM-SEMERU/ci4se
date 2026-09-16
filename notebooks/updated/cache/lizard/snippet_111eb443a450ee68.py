def restore_scoped_package_version_from_recycle_bin(self,
    package_version_details, feed_id, package_scope, unscoped_package_name,
    package_version):
    route_values = {}
    if feed_id is not None:
        route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
    if package_scope is not None:
        route_values['packageScope'] = self._serialize.url('package_scope',
            package_scope, 'str')
    if unscoped_package_name is not None:
        route_values['unscopedPackageName'] = self._serialize.url(
            'unscoped_package_name', unscoped_package_name, 'str')
    if package_version is not None:
        route_values['packageVersion'] = self._serialize.url('package_version',
            package_version, 'str')
    content = self._serialize.body(package_version_details,
        'NpmRecycleBinPackageVersionDetails')
    self._send(http_method='PATCH', location_id=
        '220f45eb-94a5-432c-902a-5b8c6372e415', version='5.0-preview.1',
        route_values=route_values, content=content)