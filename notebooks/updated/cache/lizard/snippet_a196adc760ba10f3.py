def get_partition_name(cls, region=None):
    if region is None:
        region = boto3.session.Session().region_name
    region_string = region.lower()
    if region_string.startswith('cn-'):
        return 'aws-cn'
    elif region_string.startswith('us-gov'):
        return 'aws-us-gov'
    else:
        return 'aws'