def modify(self, **kwargs):
    for key in kwargs:
        if key not in ['paused', 'resolution', 'contactids', 'sendtoemail',
            'sendtosms', 'sendtotwitter', 'sendtoiphone',
            'sendnotificationwhendown', 'notifyagainevery',
            'notifywhenbackup', 'created', 'type', 'hostname', 'status',
            'lasterrortime', 'lasttesttime', 'url', 'encryption', 'port',
            'auth', 'shouldcontain', 'shouldnotcontain', 'postdata',
            'additionalurls', 'stringtosend', 'stringtoexpect',
            'expectedip', 'nameserver', 'use_legacy_notifications', 'host',
            'alert_policy', 'autoresolve', 'probe_filters']:
            sys.stderr.write("'%s'" % key + ' is not a valid argument of' +
                """<PingdomCheck>.modify()
""")
    if any([k for k in kwargs if k in legacy_notification_parameters]):
        if 'use_legacy_notifications' in kwargs and kwargs[
            'use_legacy_notifications'] != True:
            raise Exception(
                'Cannot set legacy parameter when use_legacy_notifications is not True'
                )
        kwargs['use_legacy_notifications'] = True
    response = self.pingdom.request('PUT', 'checks/%s' % self.id, kwargs)
    return response.json()['message']