def validate(self):
    if self.job_record is None:
        self.tree.timetable.assign_job_record(self)
    next_timeperiod = time_helper.increment_timeperiod(self.time_qualifier,
        self.timeperiod)
    has_younger_sibling = next_timeperiod in self.parent.children
    all_children_skipped = True
    all_children_finished = True
    for timeperiod, child in self.children.items():
        child.validate()
        if child.job_record.is_active:
            all_children_finished = False
        if not child.job_record.is_skipped:
            all_children_skipped = False
    if all_children_finished is False and self.job_record.is_finished:
        self.tree.timetable.reprocess_tree_node(self)
    if (len(self.children) != 0 and all_children_skipped and self.tree.
        build_timeperiod is not None and has_younger_sibling is True and 
        not self.job_record.is_skipped):
        self.tree.timetable.skip_tree_node(self)