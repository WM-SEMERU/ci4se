def add_router_to_hosting_device(self, context, hosting_device_id, router_id):
    e_context = context.elevated()
    r_hd_binding_db = self._get_router_binding_info(e_context, router_id)
    if r_hd_binding_db.hosting_device_id:
        if r_hd_binding_db.hosting_device_id == hosting_device_id:
            return
        raise routertypeawarescheduler.RouterHostedByHostingDevice(router_id
            =router_id, hosting_device_id=hosting_device_id)
    rt_info = self.validate_hosting_device_router_combination(context,
        r_hd_binding_db, hosting_device_id)
    result = self.schedule_router_on_hosting_device(e_context,
        r_hd_binding_db, hosting_device_id, rt_info['slot_need'])
    if result:
        e_context.session.expire(r_hd_binding_db)
        router = self.get_router(e_context, router_id)
        self.add_type_and_hosting_device_info(e_context, router,
            r_hd_binding_db, schedule=False)
        l3_cfg_notifier = self.agent_notifiers.get(AGENT_TYPE_L3_CFG)
        if l3_cfg_notifier:
            l3_cfg_notifier.router_added_to_hosting_device(context, router)
    else:
        raise routertypeawarescheduler.RouterSchedulingFailed(router_id=
            router_id, hosting_device_id=hosting_device_id)