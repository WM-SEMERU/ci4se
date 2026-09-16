def ready(self):
    try:
        if self.is_ready():
            return 'OK', 200
        else:
            return 'FAIL', 500
    except Exception as e:
        self.app.logger.exception()
        return str(e), 500