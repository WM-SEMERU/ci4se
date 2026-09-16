def handle_response(self, response, **kwargs):
    num_401s = kwargs.pop('num_401s', 0)
    if not self.cbt_binding_tried and self.send_cbt:
        cbt_application_data = _get_channel_bindings_application_data(response)
        if cbt_application_data:
            try:
                self.cbt_struct = kerberos.channelBindings(application_data
                    =cbt_application_data)
            except AttributeError:
                self.cbt_struct = None
        self.cbt_binding_tried = True
    if self.pos is not None:
        response.request.body.seek(self.pos)
    if response.status_code == 401 and num_401s < 2:
        _r = self.handle_401(response, **kwargs)
        log.debug('handle_response(): returning %s', _r)
        log.debug('handle_response() has seen %d 401 responses', num_401s)
        num_401s += 1
        return self.handle_response(_r, num_401s=num_401s, **kwargs)
    elif response.status_code == 401 and num_401s >= 2:
        log.debug('handle_response(): returning 401 %s', response)
        return response
    else:
        _r = self.handle_other(response)
        log.debug('handle_response(): returning %s', _r)
        return _r