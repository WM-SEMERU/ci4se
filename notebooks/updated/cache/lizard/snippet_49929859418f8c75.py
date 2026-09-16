def _UpdateProcessStatus(self, process_status, identifier, status, pid,
    used_memory, display_name, number_of_consumed_sources,
    number_of_produced_sources, number_of_consumed_events,
    number_of_produced_events, number_of_consumed_event_tags,
    number_of_produced_event_tags, number_of_consumed_reports,
    number_of_produced_reports, number_of_consumed_warnings,
    number_of_produced_warnings):
    new_sources = process_status.UpdateNumberOfEventSources(
        number_of_consumed_sources, number_of_produced_sources)
    new_events = process_status.UpdateNumberOfEvents(number_of_consumed_events,
        number_of_produced_events)
    new_event_tags = process_status.UpdateNumberOfEventTags(
        number_of_consumed_event_tags, number_of_produced_event_tags)
    new_warnings = process_status.UpdateNumberOfWarnings(
        number_of_consumed_warnings, number_of_produced_warnings)
    new_reports = process_status.UpdateNumberOfEventReports(
        number_of_consumed_reports, number_of_produced_reports)
    process_status.display_name = display_name
    process_status.identifier = identifier
    process_status.pid = pid
    process_status.status = status
    process_status.used_memory = used_memory
    if (new_sources or new_events or new_event_tags or new_warnings or
        new_reports):
        process_status.last_running_time = time.time()