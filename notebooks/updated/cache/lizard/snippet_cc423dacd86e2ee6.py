def GetAmi(ec2, ami_spec):
    images = ec2.get_all_images(owners=[ami_spec.owner_id])
    requested_image = None
    for image in images:
        if image.name == ami_spec.ami_name:
            requested_image = image
            break
    return requested_image