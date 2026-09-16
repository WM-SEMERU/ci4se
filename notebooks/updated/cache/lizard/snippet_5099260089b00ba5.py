def UpdateForemanStatus(self, identifier, status, pid, used_memory,
    display_name, number_of_consumed_sources, number_of_produced_sources,
    number_of_consumed_events, number_of_produced_events,
    number_of_consumed_event_tags, number_of_produced_event_tags,
    number_of_consumed_reports, number_of_produced_reports,
    number_of_consumed_warnings, number_of_produced_warnings):
    if not self.foreman_status:
        self.foreman_status = ProcessStatus()
    self._UpdateProcessStatus(self.foreman_status, identifier, status, pid,
        used_memory, display_name, number_of_consumed_sources,
        number_of_produced_sources, number_of_consumed_events,
        number_of_produced_events, number_of_consumed_event_tags,
        number_of_produced_event_tags, number_of_consumed_reports,
        number_of_produced_reports, number_of_consumed_warnings,
        number_of_produced_warnings)