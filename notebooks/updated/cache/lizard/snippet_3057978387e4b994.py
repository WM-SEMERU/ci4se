def get_topic_sha3(event_block):
    sig = ''
    sig += event_block['name']
    if not event_block['inputs']:
        sig += '()'
        return sig
    sig += '('
    for input in event_block['inputs']:
        sig += input['type']
        sig += ','
    sig = sig[:-1]
    sig += ')'
    return sig