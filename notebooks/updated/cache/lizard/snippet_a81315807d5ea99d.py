def get_event_handlers(self, hosts, macromodulations, timeperiods, ext_cmd=
    False):
    cls = self.__class__
    if not ext_cmd and (not self.event_handler_enabled or not cls.
        enable_event_handlers):
        logger.debug('Event handler is disabled for %s', self.get_full_name())
        return
    if (not ext_cmd and self.in_scheduled_downtime and cls.
        no_event_handlers_during_downtimes):
        logger.debug(
            'Event handler will not be launched. The item %s is in a scheduled downtime'
            , self.get_full_name())
        return
    if self.event_handler is not None:
        event_handler = self.event_handler
    elif cls.global_event_handler is not None:
        event_handler = cls.global_event_handler
    else:
        return
    macroresolver = MacroResolver()
    data = self.get_data_for_event_handler(hosts)
    cmd = macroresolver.resolve_command(event_handler, data,
        macromodulations, timeperiods)
    event_h = EventHandler({'command': cmd, 'timeout': cls.
        event_handler_timeout, 'ref': self.uuid, 'reactionner_tag':
        event_handler.reactionner_tag})
    self.raise_event_handler_log_entry(event_handler)
    self.actions.append(event_h)