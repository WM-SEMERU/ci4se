def delete_releasefile(self, release):
    fp = release._releasefile.get_fullpath()
    log.info('Deleting release file %s', fp)
    delete_file(release._releasefile)
    return ActionStatus(ActionStatus.SUCCESS, msg='Deleted %s' % fp)