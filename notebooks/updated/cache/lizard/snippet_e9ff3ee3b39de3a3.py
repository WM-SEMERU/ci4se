def edit(self, hardware_id, userdata=None, hostname=None, domain=None,
    notes=None, tags=None):
    obj = {}
    if userdata:
        self.hardware.setUserMetadata([userdata], id=hardware_id)
    if tags is not None:
        self.hardware.setTags(tags, id=hardware_id)
    if hostname:
        obj['hostname'] = hostname
    if domain:
        obj['domain'] = domain
    if notes:
        obj['notes'] = notes
    if not obj:
        return True
    return self.hardware.editObject(obj, id=hardware_id)