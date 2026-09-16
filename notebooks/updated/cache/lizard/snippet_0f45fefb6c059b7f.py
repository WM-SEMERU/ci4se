def download(config, account, day, region, output):
    with open(config) as fh:
        config = yaml.safe_load(fh.read())
    jsonschema.validate(config, CONFIG_SCHEMA)
    found = None
    for info in config['accounts']:
        if info['name'] == account:
            found = info
            break
    if not found:
        log.info('Account %s not found', account)
        return
    s3 = boto3.client('s3')
    day = parse_date(day)
    key_data = dict(found)
    key_data['region'] = region
    key_data['date_fmt'] = '%s/%s/%s' % (day.year, day.month, day.day)
    key = config['key_template'] % key_data
    s3.download_file(found['bucket'], key, output + '.bz2')
    subprocess.check_call(['lbzip2', '-d', output + '.bz2'])