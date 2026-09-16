def enable(self):
    if not CrashReporter.active:
        CrashReporter.active = True
        self._excepthook = sys.excepthook
        sys.excepthook = self.exception_handler
        self.logger.info('CrashReporter: Enabled')
        if self.report_dir:
            if os.path.exists(self.report_dir):
                if self.get_offline_reports():
                    self.submit_offline_reports()
                    remaining_reports = len(self.get_offline_reports())
                    if remaining_reports and self.watcher_enabled:
                        self.start_watcher()
            else:
                os.makedirs(self.report_dir)