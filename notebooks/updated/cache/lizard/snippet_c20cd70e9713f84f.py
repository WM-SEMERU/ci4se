def update_node(self, job_record):
    if job_record.process_name not in self.process_hierarchy:
        raise ValueError(
            'unable to update the node due to unknown process: {0}'.format(
            job_record.process_name))
    time_qualifier = self.process_hierarchy[job_record.process_name
        ].process_entry.time_qualifier
    node = self._get_node(time_qualifier, job_record.timeperiod)
    node.job_record = job_record