def disable_contact_svc_notifications(self, contact):
    if contact.service_notifications_enabled:
        contact.modified_attributes |= DICT_MODATTR[
            'MODATTR_NOTIFICATIONS_ENABLED'].value
        contact.service_notifications_enabled = False
        self.send_an_element(contact.get_update_status_brok())