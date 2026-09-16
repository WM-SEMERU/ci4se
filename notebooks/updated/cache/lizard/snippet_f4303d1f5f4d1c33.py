def pull(src, dest):
    adb_full_cmd = [v.ADB_COMMAND_PREFIX, v.ADB_COMMAND_PULL, src, dest]
    return _exec_command(adb_full_cmd)