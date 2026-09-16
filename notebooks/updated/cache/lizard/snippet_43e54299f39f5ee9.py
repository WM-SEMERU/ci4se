def oldest_peer(peers):
    local_unit_no = int(os.getenv('JUJU_UNIT_NAME').split('/')[1])
    for peer in peers:
        remote_unit_no = int(peer.split('/')[1])
        if remote_unit_no < local_unit_no:
            return False
    return True