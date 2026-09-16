def file_decrypt_from_key_info(sender_key_info, blockchain_id, key_index,
    hostname, input_path, output_path, passphrase=None, config_path=
    CONFIG_PATH, wallet_keys=None):
    config_dir = os.path.dirname(config_path)
    my_key_info = file_key_lookup(blockchain_id, key_index, hostname,
        config_path=config_path, wallet_keys=wallet_keys)
    if 'error' in my_key_info:
        log.error('Failed to look up key: %s' % my_key_info['error'])
        return {'status': True, 'error': 'Failed to lookup sender key'}
    res = None
    with open(input_path, 'r') as f:
        res = blockstack_gpg.gpg_decrypt(f, output_path, sender_key_info,
            my_key_info, passphrase=passphrase, config_dir=config_dir)
    if 'error' in res:
        if res['error'] == 'Failed to decrypt data':
            log.warn('Key %s failed to decrypt' % my_key_info['key_id'])
            return {'status': True, 'error': 'Failed to decrypt with key'}
        else:
            log.error('Failed to decrypt: %s' % res['error'])
            return {'status': False, 'error': 'GPG error (%s)' % res['error']}
    return {'status': True}