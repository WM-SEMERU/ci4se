def init_app(self, app):
    self.app = app
    self.app.apscheduler = self
    self._load_config()
    self._load_jobs()
    if self.api_enabled:
        self._load_api()