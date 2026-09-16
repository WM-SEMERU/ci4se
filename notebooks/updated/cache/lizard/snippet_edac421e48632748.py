def handle_manage_name_id_request(self, name_id, new_id=None,
    new_encrypted_id='', terminate=''):
    _id = self.find_local_id(name_id)
    orig_name_id = copy.copy(name_id)
    if new_id:
        name_id.sp_provided_id = new_id.text
    elif new_encrypted_id:
        pass
    elif terminate:
        name_id.sp_provided_id = None
    else:
        return name_id
    self.remove_remote(orig_name_id)
    self.store(_id, name_id)
    return name_id