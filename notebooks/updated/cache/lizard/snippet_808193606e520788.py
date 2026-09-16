def get_jobs(self, recursive=True):
    if recursive:
        ret_dict = self.jobs.copy()
        return ret_dict
    return self.jobs