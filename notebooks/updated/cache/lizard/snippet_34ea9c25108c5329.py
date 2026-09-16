def _ensure_update_ha_compliant(self, router, current_router, r_hd_binding_db):
    if r_hd_binding_db.role == ROUTER_ROLE_HA_REDUNDANCY:
        return {ha.ENABLED: False}
    auto_enable_ha = r_hd_binding_db.router_type.ha_enabled_by_default
    requested_ha_details = router.pop(ha.DETAILS, {})
    requested_ha_enabled = router.pop(ha.ENABLED, True if 
        requested_ha_details or auto_enable_ha is True else None)
    res = {}
    ha_currently_enabled = current_router.get(ha.ENABLED, False)
    if requested_ha_enabled is True or ha_currently_enabled is True:
        if not cfg.CONF.ha.ha_support_enabled:
            raise ha.HADisabled()
        curr_ha_details = current_router.get(ha.DETAILS, {})
        if ha.TYPE in requested_ha_details:
            requested_ha_type = requested_ha_details[ha.TYPE]
            if (ha.TYPE in curr_ha_details and requested_ha_type !=
                curr_ha_details[ha.TYPE]):
                raise ha.HATypeCannotBeChanged()
            elif requested_ha_type in cfg.CONF.ha.disabled_ha_mechanisms:
                raise ha.HADisabledHAType(ha_type=requested_ha_type)
    if requested_ha_enabled:
        res[ha.ENABLED] = requested_ha_enabled
        if requested_ha_details:
            res[ha.DETAILS] = requested_ha_details
    elif requested_ha_enabled is False:
        res[ha.ENABLED] = False
    return res