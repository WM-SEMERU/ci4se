def find_by_ids(self, _ids, projection=None, **kwargs):
    id_list = [ObjectId(_id) for _id in _ids]
    if len(_ids) == 0:
        return []
    if projection is not None and list(projection.keys()) == ['_id']:
        return [self({'_id': x}, fetched_fields={'_id': True}) for x in id_list
            ]
    else:
        return self.find({'_id': {'$in': id_list}}, projection=projection,
            **kwargs)