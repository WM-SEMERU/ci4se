def load_eggs(entry_point_name):

    def _load_eggs():
        distributions, errors = working_set.find_plugins(Environment())
        for dist in distributions:
            if dist not in working_set:
                LOGGER.debug('Adding plugin %s from %s', dist, dist.location)
                working_set.add(dist)

        def _log_error(item, err):
            if isinstance(err, DistributionNotFound):
                LOGGER.debug('Skipping "%s": ("%s" not found)', item, err)
            elif isinstance(err, VersionConflict):
                LOGGER.error('Skipping "%s": (version conflict "%s")', item,
                    err)
            elif isinstance(err, UnknownExtra):
                LOGGER.error('Skipping "%s": (unknown extra "%s")', item, err)
            else:
                LOGGER.error('Skipping "%s": %s', item, err)
        for dist, err in errors.items():
            _log_error(dist, err)
        for entry in sorted(working_set.iter_entry_points(entry_point_name),
            key=lambda entry: entry.name):
            try:
                entry.load(require=True)
            except Exception as exc:
                _log_error(entry, exc)
    return _load_eggs