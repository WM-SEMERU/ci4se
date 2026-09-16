def delete_resource(self, resource, filename, allow_deletion=False):
    num_deleted = 0
    uri = resource.uri
    if (resource.timestamp is not None and resource.timestamp > self.
        last_timestamp):
        self.last_timestamp = resource.timestamp
    if allow_deletion:
        if self.dryrun:
            self.logger.info('dryrun: would delete %s -> %s' % (uri, filename))
        else:
            try:
                os.unlink(filename)
                num_deleted += 1
                self.logger.info('deleted: %s -> %s' % (uri, filename))
                self.log_event(Resource(resource=resource, change='deleted'))
            except OSError as e:
                msg = 'Failed to DELETE %s -> %s : %s' % (uri, filename, str(e)
                    )
                self.logger.warning(msg)
    else:
        self.logger.info('nodelete: would delete %s (--delete to enable)' % uri
            )
    return num_deleted