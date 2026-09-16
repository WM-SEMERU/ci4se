def _CalculateStorageCounters(self, storage_reader):
    analysis_reports_counter = collections.Counter()
    analysis_reports_counter_error = False
    event_labels_counter = collections.Counter()
    event_labels_counter_error = False
    parsers_counter = collections.Counter()
    parsers_counter_error = False
    for session in storage_reader.GetSessions():
        if isinstance(session.analysis_reports_counter, dict):
            analysis_reports_counter += collections.Counter(session.
                analysis_reports_counter)
        elif isinstance(session.analysis_reports_counter, collections.Counter):
            analysis_reports_counter += session.analysis_reports_counter
        else:
            analysis_reports_counter_error = True
        if isinstance(session.event_labels_counter, dict):
            event_labels_counter += collections.Counter(session.
                event_labels_counter)
        elif isinstance(session.event_labels_counter, collections.Counter):
            event_labels_counter += session.event_labels_counter
        else:
            event_labels_counter_error = True
        if isinstance(session.parsers_counter, dict):
            parsers_counter += collections.Counter(session.parsers_counter)
        elif isinstance(session.parsers_counter, collections.Counter):
            parsers_counter += session.parsers_counter
        else:
            parsers_counter_error = True
    storage_counters = {}
    warnings_by_path_spec = collections.Counter()
    warnings_by_parser_chain = collections.Counter()
    for warning in list(storage_reader.GetWarnings()):
        warnings_by_path_spec[warning.path_spec.comparable] += 1
        warnings_by_parser_chain[warning.parser_chain] += 1
    storage_counters['warnings_by_path_spec'] = warnings_by_path_spec
    storage_counters['warnings_by_parser_chain'] = warnings_by_parser_chain
    if not analysis_reports_counter_error:
        storage_counters['analysis_reports'] = analysis_reports_counter
    if not event_labels_counter_error:
        storage_counters['event_labels'] = event_labels_counter
    if not parsers_counter_error:
        storage_counters['parsers'] = parsers_counter
    return storage_counters