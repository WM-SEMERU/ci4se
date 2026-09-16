def file_verify(sender_blockchain_id, sender_key_id, input_path, sig,
    config_path=CONFIG_PATH, wallet_keys=None):
    config_dir = os.path.dirname(config_path)
    old_key = False
    old_key_index = 0
    sender_old_key_index = 0
    sender_key_info = file_key_lookup(sender_blockchain_id, None, None,
        key_id=sender_key_id, config_path=config_path, wallet_keys=wallet_keys)
    if 'error' in sender_key_info:
        log.error('Failed to look up sender key: %s' % sender_key_info['error']
            )
        return {'error': 'Failed to lookup sender key'}
    if 'stale_key_index' in sender_key_info.keys():
        old_key = True
        sender_old_key_index = sender_key_info['sender_key_index']
    res = blockstack_gpg.gpg_verify(input_path, sig, sender_key_info,
        config_dir=config_dir)
    if 'error' in res:
        log.error('Failed to verify from %s.%s' % (sender_blockchain_id,
            sender_key_id))
        return {'error': 'Failed to verify'}
    return {'status': True}