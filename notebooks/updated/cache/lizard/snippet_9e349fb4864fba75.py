def migrate_non_shared(vm_, target, ssh=False):
    cmd = _get_migrate_command() + ' --copy-storage-all ' + vm_ + _get_target(
        target, ssh)
    stdout = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE
        ).communicate()[0]
    return salt.utils.stringutils.to_str(stdout)