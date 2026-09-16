def do_GET(self):
    self._IncrementActiveCount()
    try:
        if self.path.startswith('/server.pem'):
            stats_collector_instance.Get().IncrementCounter(
                'frontend_http_requests', fields=['cert', 'http'])
            self.ServerPem()
        elif self.path.startswith(self.static_content_path):
            stats_collector_instance.Get().IncrementCounter(
                'frontend_http_requests', fields=['static', 'http'])
            self.ServeStatic(self.path[len(self.static_content_path):])
    finally:
        self._DecrementActiveCount()