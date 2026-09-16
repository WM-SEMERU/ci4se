def AmiName(ami_release_name, ubuntu_release_name, virtualization_type,
    mapr_version, role):
    if not role in valid_instance_roles:
        raise RuntimeError('Specified role (%s) not a valid role: %s' % (
            role, valid_instance_roles))
    if virtualization_type not in valid_virtualization_types:
        raise RuntimeError(
            'Specified virtualization type (%s) not valid: %s' % (
            virtualization_type, valid_virtualization_types))
    ami_name = 'cirrus-%s-ubuntu-%s-%s-mapr%s-%s' % (ami_release_name,
        ubuntu_release_name, virtualization_type, mapr_version, role)
    return ami_name