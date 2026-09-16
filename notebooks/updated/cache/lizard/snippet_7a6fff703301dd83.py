def up_by_time(*filters, local_dir='.', remote_dir=DEFAULT_REMOTE_DIR, count=1
    ):
    remote_files = command.map_files_raw(remote_dir=remote_dir)
    local_files = list_local_files(*filters, local_dir=local_dir)
    most_recent = sorted(local_files, key=lambda f: f.datetime)
    to_sync = most_recent[-count:]
    _notify_sync(Direction.up, to_sync)
    up_by_files(to_sync[::-1], remote_dir, remote_files)