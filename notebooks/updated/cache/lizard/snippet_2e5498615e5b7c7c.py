def match_member_id(self, member_conf, current_member_confs):
    if current_member_confs is None:
        return None
    for curr_mem_conf in current_member_confs:
        if is_same_address(member_conf['host'], curr_mem_conf['host']):
            return curr_mem_conf['_id']
    return None