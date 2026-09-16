def enable_svc_freshness_check(self, service):
    if not service.check_freshness:
        service.modified_attributes |= DICT_MODATTR[
            'MODATTR_FRESHNESS_CHECKS_ENABLED'].value
        service.check_freshness = True
        self.send_an_element(service.get_update_status_brok())