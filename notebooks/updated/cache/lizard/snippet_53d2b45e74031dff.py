def ssh_get_info(node):
    ssh_key = ''
    if node.cloud == 'aws':
        raw_key = node.extra['key_name']
        ssh_key = '-i {0}{1}.pem '.format(CONFIG_DIR, raw_key)
        ssh_user = ssh_calc_aws(node)
    elif node.cloud == 'azure':
        ssh_user = node.extra['properties']['osProfile']['adminUsername']
    elif node.cloud == 'gcp':
        items = node.extra['metadata'].get('items', [{}])
        keyname = items['key' == 'ssh-keys'].get('value', '')
        pos = keyname.find(':')
        ssh_user = keyname[0:pos]
    elif node.cloud == 'alicloud':
        ssh_user = ''
    return ssh_user, ssh_key