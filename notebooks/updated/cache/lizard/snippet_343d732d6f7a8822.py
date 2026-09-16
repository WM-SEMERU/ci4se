def _get_session(region, key, keyid, profile):
    if profile:
        if isinstance(profile, six.string_types):
            _profile = __salt__['config.option'](profile)
        elif isinstance(profile, dict):
            _profile = profile
        key = _profile.get('key', None)
        keyid = _profile.get('keyid', None)
        region = _profile.get('region', None)
    if not region and __salt__['config.option']('datapipeline.region'):
        region = __salt__['config.option']('datapipeline.region')
    if not region:
        region = 'us-east-1'
    return boto3.session.Session(region_name=region, aws_secret_access_key=
        key, aws_access_key_id=keyid)