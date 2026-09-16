def _exclusively_used(self, context, hosting_device, tenant_id):
    return context.session.query(hd_models.SlotAllocation).filter(hd_models
        .SlotAllocation.hosting_device_id == hosting_device['id'], 
        hd_models.SlotAllocation.logical_resource_owner != tenant_id).first(
        ) is None