def LookupCirrusAmi(ec2, instance_type, ubuntu_release_name, mapr_version,
    role, ami_release_name, ami_owner_id):
    if not role in valid_instance_roles:
        raise RuntimeError('Specified role (%s) not a valid role: %s' % (
            role, valid_instance_roles))
    virtualization_type = 'paravirtual'
    if IsHPCInstanceType(instance_type):
        virtualization_type = 'hvm'
    assert ami_owner_id
    images = ec2.get_all_images(owners=[ami_owner_id])
    ami = None
    ami_name = AmiName(ami_release_name, ubuntu_release_name,
        virtualization_type, mapr_version, role)
    for image in images:
        if image.name == ami_name:
            ami = image
            break
    return ami