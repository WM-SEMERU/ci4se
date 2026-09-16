def load_by_keygrip(pubkey_bytes, keygrip):
    stream = io.BytesIO(pubkey_bytes)
    packets = list(parse_packets(stream))
    packets_per_pubkey = []
    for p in packets:
        if p['type'] == 'pubkey':
            packets_per_pubkey.append([])
        packets_per_pubkey[-1].append(p)
    for packets in packets_per_pubkey:
        user_ids = [p for p in packets if p['type'] == 'user_id']
        for p in packets:
            if p.get('keygrip') == keygrip:
                return p, user_ids
    raise KeyError('{} keygrip not found'.format(util.hexlify(keygrip)))