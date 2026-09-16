def ajax_get_service(self):
    uid = self.request.form.get('uid', None)
    if uid is None:
        return self.error('Invalid UID', status=400)
    service = self.get_object_by_uid(uid)
    if not service:
        return self.error('Service not found', status=404)
    info = self.get_service_info(service)
    return info