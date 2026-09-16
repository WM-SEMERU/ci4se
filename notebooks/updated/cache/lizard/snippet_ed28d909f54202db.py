def event(self, chunk_ret, length, fire_event=False):
    if not self.opts.get('local') and (self.opts.get('state_events', True) or
        fire_event):
        if not self.opts.get('master_uri'):
            ev_func = (lambda ret, tag, preload=None: salt.utils.event.
                get_master_event(self.opts, self.opts['sock_dir'], listen=
                False).fire_event(ret, tag))
        else:
            ev_func = self.functions['event.fire_master']
        ret = {'ret': chunk_ret}
        if fire_event is True:
            tag = salt.utils.event.tagify([self.jid, self.opts['id'], six.
                text_type(chunk_ret['name'])], 'state_result')
        elif isinstance(fire_event, six.string_types):
            tag = salt.utils.event.tagify([self.jid, self.opts['id'], six.
                text_type(fire_event)], 'state_result')
        else:
            tag = salt.utils.event.tagify([self.jid, 'prog', self.opts['id'
                ], six.text_type(chunk_ret['__run_num__'])], 'job')
            ret['len'] = length
        preload = {'jid': self.jid}
        ev_func(ret, tag, preload=preload)