def disable(message=None):
    puppet = _Puppet()
    if os.path.isfile(puppet.disabled_lockfile):
        return False
    else:
        with salt.utils.files.fopen(puppet.disabled_lockfile, 'w') as lockfile:
            try:
                msg = '{{"disabled_message":"{0}"}}'.format(message
                    ) if message is not None else '{}'
                lockfile.write(salt.utils.stringutils.to_str(msg))
                lockfile.close()
                return True
            except (IOError, OSError) as exc:
                msg = 'Failed to disable: {0}'.format(exc)
                log.error(msg)
                raise CommandExecutionError(msg)