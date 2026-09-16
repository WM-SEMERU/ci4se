def grouped_items(self, folder_id, subfolder_id, ann_id=None):
    d = defaultdict(list)
    for cid, subid in self.items(folder_id, subfolder_id, ann_id=ann_id):
        d[cid].append(subid)
    return d