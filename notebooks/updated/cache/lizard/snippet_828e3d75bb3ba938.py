def notify_observers(self, event=None, msg=None):
    for observer, events in list(self._observers.items()):
        if events is None or event is None or event in events:
            try:
                observer(self, event, msg)
            except (Exception,) as ex:
                self.unregister_observer(observer)
                errmsg = (
                    "Exception in message dispatch: Handler '{0}' unregistered for event '{1}'  "
                    .format(observer.__class__.__name__, event))
                LOG.error(errmsg, exc_info=ex)