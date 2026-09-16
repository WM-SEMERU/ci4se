def config_files():
    sensu_loaded_tempfile = os.environ.get('SENSU_LOADED_TEMPFILE')
    sensu_config_files = os.environ.get('SENSU_CONFIG_FILES')
    sensu_v1_config = '/etc/sensu/config.json'
    sensu_v1_confd = '/etc/sensu/conf.d'
    if sensu_loaded_tempfile and os.path.isfile(sensu_loaded_tempfile):
        with open(sensu_loaded_tempfile, 'r') as tempfile:
            contents = tempfile.read()
            return contents.split(':')
    elif sensu_config_files:
        return sensu_config_files.split(':')
    else:
        files = []
        filenames = []
        if os.path.isfile(sensu_v1_config):
            files = [sensu_v1_config]
        if os.path.isdir(sensu_v1_confd):
            filenames = [f for f in os.listdir(sensu_v1_confd) if os.path.
                splitext(f)[1] == '.json']
            for filename in filenames:
                files.append('{}/{}'.format(sensu_v1_confd, filename))
        return files