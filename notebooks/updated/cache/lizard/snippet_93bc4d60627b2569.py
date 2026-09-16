def run_delete_sm(self, tenant_id, fw_dict, is_fw_virt):
    ret = True
    serv_obj = self.get_service_obj(tenant_id)
    state = serv_obj.get_state()
    new_state = serv_obj.fixup_state(fw_const.FW_DEL_OP, state)
    serv_obj.store_local_final_result(fw_const.RESULT_FW_DELETE_INIT)
    if state != new_state:
        state = new_state
        serv_obj.store_state(state)
    while ret:
        try:
            ret = self.fabric_fsm[state][1](tenant_id, fw_dict, is_fw_virt=
                is_fw_virt)
        except Exception as exc:
            LOG.error('Exception %(exc)s for state %(state)s', {'exc': str(
                exc), 'state': fw_const.fw_state_fn_del_dict.get(state)})
            ret = False
        if ret:
            LOG.info('State %s return successfully', fw_const.
                fw_state_fn_del_dict.get(state))
        if state == fw_const.INIT_STATE:
            break
        state = self.get_next_state(state, ret, fw_const.FW_DEL_OP)
        serv_obj.store_state(state)
    return ret