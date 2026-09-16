def disable_passive_svc_checks(self, service):
    if service.passive_checks_enabled:
        service.modified_attributes |= DICT_MODATTR[
            'MODATTR_PASSIVE_CHECKS_ENABLED'].value
        service.passive_checks_enabled = False
        self.send_an_element(service.get_update_status_brok())