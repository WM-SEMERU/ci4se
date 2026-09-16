def subtopics(store, folders, folder_id, subfolder_id, ann_id=None):
    items = folders.grouped_items(folder_id, subfolder_id, ann_id=ann_id)
    fcs = dict([(cid, fc) for cid, fc in store.get_many(items.keys())])
    for cid, subids in items.iteritems():
        fc = fcs[cid]
        for subid in subids:
            try:
                data = typed_subtopic_data(fc, subid)
            except KeyError:
                continue
            yield cid, subid, fc['meta_url'], subtopic_type(subid), data