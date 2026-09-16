def disable_host_notifications(self, host):
    if host.notifications_enabled:
        host.modified_attributes |= DICT_MODATTR[
            'MODATTR_NOTIFICATIONS_ENABLED'].value
        host.notifications_enabled = False
        self.send_an_element(host.get_update_status_brok())