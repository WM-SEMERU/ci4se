def get_billing_report_firmware_updates(self, month, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_billing_report_firmware_updates_with_http_info(month,
            **kwargs)
    else:
        data = self.get_billing_report_firmware_updates_with_http_info(month,
            **kwargs)
        return data