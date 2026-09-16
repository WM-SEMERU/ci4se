def _get_data_volumes(vm_):
    ret = []
    volumes = vm_['volumes']
    for key, value in six.iteritems(volumes):
        if 'disk_size' not in volumes[key].keys():
            raise SaltCloudConfigError(
                "The volume '{0}' is missing 'disk_size'".format(key))
        if 'disk_type' not in volumes[key].keys():
            volumes[key]['disk_type'] = 'HDD'
        volume = Volume(name=key, size=volumes[key]['disk_size'], disk_type
            =volumes[key]['disk_type'], licence_type='OTHER')
        if 'disk_availability_zone' in volumes[key].keys():
            volume.availability_zone = volumes[key]['disk_availability_zone']
        ret.append(volume)
    return ret