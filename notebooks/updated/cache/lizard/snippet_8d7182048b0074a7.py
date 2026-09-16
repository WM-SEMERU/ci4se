def get_cloud_init_mime(cloud_init):
    if isinstance(cloud_init, six.string_types):
        cloud_init = salt.utils.json.loads(cloud_init)
    _cloud_init = email.mime.multipart.MIMEMultipart()
    if 'boothooks' in cloud_init:
        for script_name, script in six.iteritems(cloud_init['boothooks']):
            _script = email.mime.text.MIMEText(script, 'cloud-boothook')
            _cloud_init.attach(_script)
    if 'scripts' in cloud_init:
        for script_name, script in six.iteritems(cloud_init['scripts']):
            _script = email.mime.text.MIMEText(script, 'x-shellscript')
            _cloud_init.attach(_script)
    if 'cloud-config' in cloud_init:
        cloud_config = cloud_init['cloud-config']
        _cloud_config = email.mime.text.MIMEText(salt.utils.yaml.safe_dump(
            cloud_config, default_flow_style=False), 'cloud-config')
        _cloud_init.attach(_cloud_config)
    return _cloud_init.as_string()