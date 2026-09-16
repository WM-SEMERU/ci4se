def get_outbox_fax(self, outbox_fax_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async'):
        return self.get_outbox_fax_with_http_info(outbox_fax_id, **kwargs)
    else:
        data = self.get_outbox_fax_with_http_info(outbox_fax_id, **kwargs)
        return data