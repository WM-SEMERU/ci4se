def reset_context(**options):
    local_context._options = {}
    local_context._options.update(options)
    log.debug('New TelluricContext context %r created', local_context._options)