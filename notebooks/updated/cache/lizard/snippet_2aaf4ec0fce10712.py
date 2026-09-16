def setup_dns(endpoint):
    print('Setting up DNS...')
    yass = Yass(CWD)
    target = endpoint.lower()
    sitename = yass.sitename
    if not sitename:
        raise ValueError('Missing site name')
    endpoint = yass.config.get('hosting.%s' % target)
    if not endpoint:
        raise ValueError('%s endpoint is missing in the hosting config' %
            target.upper())
    if target == 's3':
        p = publisher.S3Website(sitename=sitename, aws_access_key_id=
            endpoint.get('aws_access_key_id'), aws_secret_access_key=
            endpoint.get('aws_secret_access_key'), region=endpoint.get(
            'aws_region'))
        print('Setting AWS Route53 for: %s ...' % p.sitename)
        p.setup_dns()
        print('')
        print('Yass! Route53 setup successfully!')
        print('You can now visit the site at :')
        print(p.sitename_endpoint)
    footer()