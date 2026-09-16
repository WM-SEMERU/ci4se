def validate(self):
    if len(self.ind_nodes()) == 0:
        return False, 'no independent nodes detected'
    try:
        self.topological_sort()
    except ValueError as e:
        return False, str(e)
    return True, 'valid'