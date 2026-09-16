def get_distribution_id(vm_):
    r
    distributions = _query('avail', 'distributions')['DATA']
    vm_image_name = config.get_cloud_config_value('image', vm_, __opts__)
    distro_id = ''
    for distro in distributions:
        if vm_image_name == distro['LABEL']:
            distro_id = distro['DISTRIBUTIONID']
            return distro_id
    if not distro_id:
        raise SaltCloudNotFound(
            """The DistributionID for the '{0}' profile could not be found.
The '{1}' instance could not be provisioned. The following distributions are available:
{2}"""
            .format(vm_image_name, vm_['name'], pprint.pprint(sorted([
            distro['LABEL'].encode(__salt_system_encoding__) for distro in
            distributions]))))