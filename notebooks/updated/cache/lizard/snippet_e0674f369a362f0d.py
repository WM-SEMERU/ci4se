def _rt_state_update(route_table_id, dcidr, router_ip='(none)', instance_id
    ='(none)', eni_id='(none)', old_router_ip='(none)', msg='(none)'):
    buf = 'inst: %s, eni: %s, r_ip: %-15s, o_r_ip: %-15s, msg: %s' % (
        instance_id, eni_id, router_ip, old_router_ip, msg)
    CURRENT_STATE.vpc_state.setdefault('route_tables', {}).setdefault(
        route_table_id, {})[dcidr] = buf