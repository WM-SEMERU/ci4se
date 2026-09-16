def run_configurations(callback, sections_reader):
    base = dict(OPTIONS)
    sections = sections_reader()
    if sections is None:
        logger.info(
            'Configuration not found in .ini files. Running with default settings'
            )
        recompile()
    elif sections == []:
        logger.info('Configuration does not match current runtime. Exiting')
    results = []
    for section, options in sections:
        OPTIONS.clear()
        OPTIONS.update(base)
        OPTIONS.update(options)
        logger.debug('Running configuration from section "%s". OPTIONS: %r',
            section, OPTIONS)
        results.append(callback())
    return results