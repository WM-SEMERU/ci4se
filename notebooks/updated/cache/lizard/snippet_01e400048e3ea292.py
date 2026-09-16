def link_cloud(self, username=None, password=None, device_id=None):
    reg = ComponentRegistry()
    domain = self.get('cloud:server')
    if username is None:
        prompt_str = 'Please enter your IOTile.cloud email: '
        username = input(prompt_str)
    if password is None:
        prompt_str = 'Please enter your IOTile.cloud password: '
        password = getpass.getpass(prompt_str)
    cloud = Api(domain=domain)
    ok_resp = cloud.login(email=username, password=password)
    if not ok_resp:
        raise ArgumentError('Could not login to iotile.cloud as user %s' %
            username)
    reg.set_config('arch:cloud_user', cloud.username)
    reg.set_config('arch:cloud_token', cloud.token)
    reg.set_config('arch:cloud_token_type', cloud.token_type)
    if device_id is not None:
        cloud = IOTileCloud()
        cloud.impersonate_device(device_id)