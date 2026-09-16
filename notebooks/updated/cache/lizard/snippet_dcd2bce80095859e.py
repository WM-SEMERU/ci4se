def enable_svc_event_handler(self, service):
    if not service.event_handler_enabled:
        service.modified_attributes |= DICT_MODATTR[
            'MODATTR_EVENT_HANDLER_ENABLED'].value
        service.event_handler_enabled = True
        self.send_an_element(service.get_update_status_brok())