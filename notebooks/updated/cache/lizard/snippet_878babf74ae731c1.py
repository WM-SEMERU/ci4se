def get_child_jobs(self):
    if self.info is None:
        self.get_info()
    if self.children is not None:
        return self.children
    elif 'children' in self.info:
        child_list = []
        for child in self.info['children']['items']:
            child_job = GPJob(self.server_data, child['jobId'])
            child_job.info = child
            child_job.load_info()
            child_list.append(child_job)
        return child_list
    else:
        return []