def create(cls, name, size, type, quantity, duration, datacenter, vhosts,
    password, snapshot_profile, background, sshkey):
    if not background and not cls.intty():
        background = True
    datacenter_id_ = int(Datacenter.usable_id(datacenter))
    paas_params = {'name': name, 'size': size, 'type': type, 'duration':
        duration, 'datacenter_id': datacenter_id_}
    if password:
        paas_params['password'] = password
    if quantity:
        paas_params['quantity'] = quantity
    paas_params.update(cls.convert_sshkey(sshkey))
    if snapshot_profile:
        paas_params['snapshot_profile'] = snapshot_profile
    result = cls.call('paas.create', paas_params)
    if not background:
        cls.echo('Creating your PaaS instance.')
        cls.display_progress(result)
        cls.echo('Your PaaS instance %s has been created.' % name)
    if vhosts:
        paas_info = cls.info(name)
        Vhost.create(paas_info, vhosts, True, background)
    return result