def ConvertCloudMetadataResponsesToCloudInstance(metadata_responses):
    if metadata_responses.instance_type == 'GOOGLE':
        cloud_instance = GoogleCloudInstance()
        result = CloudInstance(cloud_type='GOOGLE', google=cloud_instance)
    elif metadata_responses.instance_type == 'AMAZON':
        cloud_instance = AmazonCloudInstance()
        result = CloudInstance(cloud_type='AMAZON', amazon=cloud_instance)
    else:
        raise ValueError('Unknown cloud instance type: %s' %
            metadata_responses.instance_type)
    for cloud_metadata in metadata_responses.responses:
        setattr(cloud_instance, cloud_metadata.label, cloud_metadata.text)
    if result.cloud_type == 'GOOGLE':
        cloud_instance.unique_id = MakeGoogleUniqueID(cloud_instance)
    return result