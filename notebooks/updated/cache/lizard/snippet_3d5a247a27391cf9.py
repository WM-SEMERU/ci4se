def delete_all(self):
    for status, keys in six.iteritems(self.list_keys()):
        for key in keys:
            try:
                os.remove(os.path.join(self.opts['pki_dir'], status, key))
                eload = {'result': True, 'act': 'delete', 'id': key}
                self.event.fire_event(eload, salt.utils.event.tagify(prefix
                    ='key'))
            except (OSError, IOError):
                pass
    self.check_minion_cache()
    if self.opts.get('rotate_aes_key'):
        salt.crypt.dropfile(self.opts['cachedir'], self.opts['user'])
    return self.list_keys()