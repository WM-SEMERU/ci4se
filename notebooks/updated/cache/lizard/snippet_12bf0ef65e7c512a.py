def validate_svc_catalog_endpoint_data(self, expected, actual,
    openstack_release=None):
    validation_function = self.validate_v2_svc_catalog_endpoint_data
    xenial_queens = OPENSTACK_RELEASES_PAIRS.index('xenial_queens')
    if openstack_release and openstack_release >= xenial_queens:
        validation_function = self.validate_v3_svc_catalog_endpoint_data
        expected = self.convert_svc_catalog_endpoint_data_to_v3(expected)
    return validation_function(expected, actual)