def announce(self, msg):
    self.print_if_verbose('{} -> {}'.format(self.network_uid, msg.__class__
        .__name__))
    self.__trigger_event__(event_class=self.MessageAnnounced, msg=msg)