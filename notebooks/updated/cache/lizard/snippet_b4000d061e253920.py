def _obtain_health_pills_at_step(self, events_directory, node_names, step):
    pattern = os.path.join(events_directory, _DEBUGGER_EVENTS_GLOB_PATTERN)
    file_paths = glob.glob(pattern)
    if not file_paths:
        raise IOError('No events files found that matches the pattern %r.' %
            pattern)
    file_paths.sort()
    mapping = collections.defaultdict(list)
    node_name_set = frozenset(node_names)
    for file_path in file_paths:
        should_stop = self._process_health_pill_event(node_name_set,
            mapping, step, file_path)
        if should_stop:
            break
    return mapping