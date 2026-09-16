def get_default_config(self):
    default_config = super(SNMPInterfaceCollector, self).get_default_config()
    default_config['path'] = 'interface'
    default_config['byte_unit'] = ['bit', 'byte']
    return default_config