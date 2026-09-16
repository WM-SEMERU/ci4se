def kernel_status(self, user_name, kernel_slug, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.kernel_status_with_http_info(user_name, kernel_slug, **
            kwargs)
    else:
        data = self.kernel_status_with_http_info(user_name, kernel_slug, **
            kwargs)
        return data