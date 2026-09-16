def identity(self):
    if self.dataset is None:
        s = object_session(self)
        ds = s.query(Dataset).filter(Dataset.id_ == self.d_id).one()
    else:
        ds = self.dataset
    d = {'id': self.id, 'vid': self.vid, 'name': self.name, 'vname': self.
        vname, 'ref': self.ref, 'space': self.space, 'time': self.time,
        'table': self.table_name, 'grain': self.grain, 'variant': self.
        variant, 'segment': self.segment, 'format': self.format if self.
        format else 'db'}
    return PartitionIdentity.from_dict(dict(list(ds.dict.items()) + list(d.
        items())))