def load_ldap_config(self):
    try:
        with open('{}/ldap_info.yaml'.format(self.config_dir), 'r') as FILE:
            config = yaml.load(FILE)
            self.host = config['server']
            self.user_dn = config['user_dn']
            self.port = config['port']
            self.basedn = config['basedn']
            self.mail_domain = config['mail_domain']
            self.service_ou = config['service_ou']
    except OSError as err:
        print('{}: Config file ({}/ldap_info.yaml) not found'.format(type(
            err), self.config_dir))