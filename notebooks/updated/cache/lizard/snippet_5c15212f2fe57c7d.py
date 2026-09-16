def set_status(self, status, add_section=True):
    status = str(status)
    if add_section:
        self.section(status)
    self.job_add_status('status', status)