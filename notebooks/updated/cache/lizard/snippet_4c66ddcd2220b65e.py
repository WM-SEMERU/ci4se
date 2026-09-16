def rhsm_register(self, rhsm):
    login = rhsm.get('login')
    password = rhsm.get('password', os.environ.get('RHN_PW'))
    pool_id = rhsm.get('pool_id')
    self.run('rm /etc/pki/product/69.pem', ignore_error=True)
    custom_log = (
        'subscription-manager register --username %s --password *******' %
        login)
    self.run('subscription-manager register --username %s --password "%s"' %
        (login, password), success_status=(0, 64), custom_log=custom_log,
        retry=3)
    if pool_id:
        self.run('subscription-manager attach --pool %s' % pool_id)
    else:
        self.run('subscription-manager attach --auto')
    self.rhsm_active = True