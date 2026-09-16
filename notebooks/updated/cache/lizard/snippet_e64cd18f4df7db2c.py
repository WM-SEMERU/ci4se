def to_json(self):
    capsule = {}
    capsule['Hierarchy'] = []
    for dying, (persistence, surviving, saddle) in self.merge_sequence.items():
        capsule['Hierarchy'].append({'Dying': dying, 'Persistence':
            persistence, 'Surviving': surviving, 'Saddle': saddle})
    capsule['Partitions'] = []
    base = np.array([None, None] * len(self.Y)).reshape(-1, 2)
    for (min_index, max_index), items in self.base_partitions.items():
        base[(items), :] = [min_index, max_index]
    capsule['Partitions'] = base.tolist()
    return json.dumps(capsule)