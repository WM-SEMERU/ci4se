def fast_sync_sign_snapshot(snapshot_path, private_key, first=False):
    if not os.path.exists(snapshot_path):
        log.error('No such file or directory: {}'.format(snapshot_path))
        return False
    file_size = 0
    payload_size = 0
    write_offset = 0
    try:
        sb = os.stat(snapshot_path)
        file_size = sb.st_size
        assert file_size > 8
    except Exception as e:
        log.exception(e)
        return False
    num_sigs = 0
    snapshot_hash = None
    with open(snapshot_path, 'r+') as f:
        if not first:
            info = fast_sync_inspect(f)
            if 'error' in info:
                log.error('Failed to inspect {}: {}'.format(snapshot_path,
                    info['error']))
                return False
            num_sigs = len(info['signatures'])
            write_offset = info['sig_append_offset']
            payload_size = info['payload_size']
        else:
            write_offset = file_size
            num_sigs = 0
            payload_size = file_size
        privkey_hex = keylib.ECPrivateKey(private_key).to_hex()
        hash_hex = get_file_hash(f, hashlib.sha256, fd_len=payload_size)
        sigb64 = sign_digest(hash_hex, privkey_hex, hashfunc=hashlib.sha256)
        if BLOCKSTACK_TEST:
            log.debug('Signed {} with {} to make {}'.format(hash_hex,
                keylib.ECPrivateKey(private_key).public_key().to_hex(), sigb64)
                )
        f.seek(write_offset, os.SEEK_SET)
        f.write(sigb64)
        f.write('{:08x}'.format(len(sigb64)))
        num_sigs += 1
        f.write('{:08x}'.format(num_sigs))
        f.flush()
        os.fsync(f.fileno())
    return True