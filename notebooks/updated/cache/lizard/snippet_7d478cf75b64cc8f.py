def list_mutating_webhook_configuration(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.list_mutating_webhook_configuration_with_http_info(**kwargs
            )
    else:
        data = self.list_mutating_webhook_configuration_with_http_info(**kwargs
            )
        return data