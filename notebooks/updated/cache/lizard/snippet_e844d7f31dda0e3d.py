def get_default_config(self):
    config = super(UserScriptsCollector, self).get_default_config()
    config.update({'path': '.', 'scripts_path':
        '/etc/diamond/user_scripts/', 'floatprecision': 4})
    return config