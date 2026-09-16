def iteryaml(self, *args, **kwargs):
    from rowgenerators.rowpipe.json import VTEncoder
    import yaml
    if 'cls' not in kwargs:
        kwargs['cls'] = VTEncoder
    for s in self.iterstruct:
        yield yaml.safe_dump(s)