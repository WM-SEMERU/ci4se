def is_request_sent(request, relation='ceph'):
    states = get_request_states(request, relation=relation)
    for rid in states.keys():
        if not states[rid]['sent']:
            return False
    return True