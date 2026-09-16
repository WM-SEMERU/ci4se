def dependent_on_composite_state(self, job_record):
    assert isinstance(job_record, Job)
    tree = self.get_tree(job_record.process_name)
    node = tree.get_node(job_record.process_name, job_record.timeperiod)
    return node.dependent_on_composite_state()