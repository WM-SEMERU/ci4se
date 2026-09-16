def _firmware_update(firmwarefile='', host='', directory=''):
    dest = os.path.join(directory, firmwarefile[7:])
    __salt__['cp.get_file'](firmwarefile, dest)
    username = __pillar__['proxy']['admin_user']
    password = __pillar__['proxy']['admin_password']
    __salt__['dracr.update_firmware'](dest, host=host, admin_username=
        username, admin_password=password)