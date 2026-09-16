def compute_actor_handle_id(actor_handle_id, num_forks):
    assert isinstance(actor_handle_id, ActorHandleID)
    handle_id_hash = hashlib.sha1()
    handle_id_hash.update(actor_handle_id.binary())
    handle_id_hash.update(str(num_forks).encode('ascii'))
    handle_id = handle_id_hash.digest()
    return ActorHandleID(handle_id)