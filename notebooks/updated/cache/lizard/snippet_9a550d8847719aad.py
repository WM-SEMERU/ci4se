def restore_backup(path, backup_id):
    path = os.path.expanduser(path)
    ret = {'result': False, 'comment': "Invalid backup_id '{0}'".format(
        backup_id)}
    try:
        if len(six.text_type(backup_id)) == len(six.text_type(int(backup_id))):
            backup = list_backups(path)[int(backup_id)]
        else:
            return ret
    except ValueError:
        return ret
    except KeyError:
        ret['comment'] = "backup_id '{0}' does not exist for {1}".format(
            backup_id, path)
        return ret
    salt.utils.files.backup_minion(path, _get_bkroot())
    try:
        shutil.copyfile(backup['Location'], path)
    except IOError as exc:
        ret['comment'] = 'Unable to restore {0} to {1}: {2}'.format(backup[
            'Location'], path, exc)
        return ret
    else:
        ret['result'] = True
        ret['comment'] = 'Successfully restored {0} to {1}'.format(backup[
            'Location'], path)
    if not salt.utils.platform.is_windows():
        try:
            fstat = os.stat(path)
        except (OSError, IOError):
            ret['comment'] += ', but was unable to set ownership'
        else:
            os.chown(path, fstat.st_uid, fstat.st_gid)
    return ret