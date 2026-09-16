def check(self, targets, topological_order=False):
    all_vts = self.wrap_targets(targets, topological_order=topological_order)
    invalid_vts = [vt for vt in all_vts if not vt.valid]
    return InvalidationCheck(all_vts, invalid_vts)