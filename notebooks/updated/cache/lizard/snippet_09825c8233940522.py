def _create_invokeScript(self, network_file_path, commands, files_map):
    LOG.debug('Creating invokeScript shell in the folder %s' %
        network_file_path)
    invokeScript = 'invokeScript.sh'
    conf = '#!/bin/bash \n'
    command = commands
    for file in files_map:
        target_path = file['target_path']
        source_file = file['source_file']
        command += 'mv ' + source_file + ' ' + target_path + '\n'
    command += 'sleep 2\n'
    command += '/bin/bash /tmp/znetconfig.sh\n'
    command += 'rm -rf invokeScript.sh\n'
    scriptfile = os.path.join(network_file_path, invokeScript)
    with open(scriptfile, 'w') as f:
        f.write(conf)
        f.write(command)