def restore_db(release=None):
    if not release:
        release = paths.get_current_release_name()
    if not release:
        raise Exception('Release %s was not found' % release)
    backup_file = 'postgresql/%s.sql.gz' % release
    backup_path = paths.get_backup_path(backup_file)
    if not env.exists(backup_path):
        raise Exception('Backup file %s not found' % backup_path)
    with context_managers.shell_env(PGPASSWORD=env.psql_password):
        env.run("pg_restore --clean -h localhost -d %s -U %s '%s'" % (env.
            psql_db, env.psql_user, backup_path))