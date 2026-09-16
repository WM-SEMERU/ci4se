def cleanup_releases(limit=5):
    init_tasks()
    max_versions = limit + 1
    env.run('ls -dt %s/*/ | tail -n +%s | xargs rm -rf' % (paths.
        get_releases_path(), max_versions))