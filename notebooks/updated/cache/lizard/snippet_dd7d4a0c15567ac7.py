def send_data_message(self, condition=None, collapse_key=None,
    delay_while_idle=False, time_to_live=None, restricted_package_name=None,
    low_priority=False, dry_run=False, data_message=None, content_available
    =None, api_key=None, timeout=5, json_encoder=None):
    from .fcm import fcm_send_single_device_data_message
    result = fcm_send_single_device_data_message(registration_id=str(self.
        registration_id), condition=condition, collapse_key=collapse_key,
        delay_while_idle=delay_while_idle, time_to_live=time_to_live,
        restricted_package_name=restricted_package_name, low_priority=
        low_priority, dry_run=dry_run, data_message=data_message,
        content_available=content_available, api_key=api_key, timeout=
        timeout, json_encoder=json_encoder)
    self._deactivate_device_on_error_result(result)
    return result