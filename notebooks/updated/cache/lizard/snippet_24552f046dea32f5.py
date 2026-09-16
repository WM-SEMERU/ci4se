def get_browser_log(self, levels=None):
    logs = self.driver.get_log('browser')
    self.browser_logs += logs
    if levels is not None:
        logs = [entry for entry in logs if entry.get('level') in levels]
    return logs