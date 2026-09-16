def get_billing_report_active_devices(self, month, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_billing_report_active_devices_with_http_info(month,
            **kwargs)
    else:
        data = self.get_billing_report_active_devices_with_http_info(month,
            **kwargs)
        return data