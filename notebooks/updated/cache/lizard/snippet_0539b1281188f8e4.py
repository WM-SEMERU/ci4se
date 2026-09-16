def tree(self, subject_ids=None, visit_ids=None, **kwargs):
    return Tree.construct(self, *self.find_data(subject_ids=subject_ids,
        visit_ids=visit_ids), **kwargs)