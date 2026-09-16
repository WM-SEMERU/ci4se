def _get_fw(self, msg, updates, req_fw_type=None, req_fw_ver=None):
    fw_type = None
    fw_ver = None
    if not isinstance(updates, tuple):
        updates = updates,
    for store in updates:
        fw_id = store.pop(msg.node_id, None)
        if fw_id is not None:
            fw_type, fw_ver = fw_id
            updates[-1][msg.node_id] = fw_id
            break
    if fw_type is None or fw_ver is None:
        _LOGGER.debug('Node %s is not set for firmware update', msg.node_id)
        return None, None, None
    if req_fw_type is not None and req_fw_ver is not None:
        fw_type, fw_ver = req_fw_type, req_fw_ver
    fware = self.firmware.get((fw_type, fw_ver))
    if fware is None:
        _LOGGER.debug('No firmware of type %s and version %s found',
            fw_type, fw_ver)
        return None, None, None
    return fw_type, fw_ver, fware