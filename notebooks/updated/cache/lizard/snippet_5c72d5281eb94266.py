def run(self):
    try:
        while self.py3_wrapper.running:
            event_str = self.poller_inp.readline()
            if not event_str:
                continue
            try:
                if event_str[0] == ',':
                    event_str = event_str[1:]
                event = loads(event_str)
                self.dispatch_event(event)
            except Exception:
                self.py3_wrapper.report_exception('Event failed')
    except:
        err = 'Events thread died, click events are disabled.'
        self.py3_wrapper.report_exception(err, notify_user=False)
        self.py3_wrapper.notify_user(err, level='warning')