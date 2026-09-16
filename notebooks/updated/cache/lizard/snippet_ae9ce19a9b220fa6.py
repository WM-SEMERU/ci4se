def status():
    for plugin, package, filename in available_migrations():
        migration = get_migration(plugin, filename)
        if migration:
            status = green(migration['date'].strftime(DATE_FORMAT))
        else:
            status = yellow('Not applied')
        log_status(plugin, filename, status)