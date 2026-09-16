def sync_status(self):
    status = None
    try:
        try:
            self.api.doi_get(self.pid.pid_value)
            status = PIDStatus.REGISTERED
        except DataCiteGoneError:
            status = PIDStatus.DELETED
        except DataCiteNoContentError:
            status = PIDStatus.REGISTERED
        except DataCiteNotFoundError:
            pass
        if status is None:
            try:
                self.api.metadata_get(self.pid.pid_value)
                status = PIDStatus.RESERVED
            except DataCiteGoneError:
                status = PIDStatus.DELETED
            except DataCiteNoContentError:
                status = PIDStatus.REGISTERED
            except DataCiteNotFoundError:
                pass
    except (DataCiteError, HttpError):
        logger.exception('Failed to sync status from DataCite', extra=dict(
            pid=self.pid))
        raise
    if status is None:
        status = PIDStatus.NEW
    self.pid.sync_status(status)
    logger.info('Successfully synced status from DataCite', extra=dict(pid=
        self.pid))
    return True