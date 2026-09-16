def disable_reporting(self):
    if self.status == Stats.DISABLED:
        return
    if not self.disableable:
        logger.critical("Can't disable reporting")
        return
    self.status = Stats.DISABLED
    self.write_config(self.status)
    if os.path.exists(self.location):
        old_reports = [f for f in os.listdir(self.location) if f.startswith
            ('report_')]
        for old_filename in old_reports:
            fullname = os.path.join(self.location, old_filename)
            os.remove(fullname)
        logger.info('Deleted %d pending reports', len(old_reports))