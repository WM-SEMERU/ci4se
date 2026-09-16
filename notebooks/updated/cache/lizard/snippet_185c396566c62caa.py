def duplicate(self, b):
    on = b.identity.on
    on.revision = on.revision + 1
    try:
        extant = self.bundle(str(on))
        if extant:
            raise ConflictError('Already have a bundle with vid: {}'.format
                (str(on)))
    except NotFoundError:
        pass
    d = b.dataset.dict
    d['revision'] = on.revision
    d['vid'] = str(on)
    del d['name']
    del d['vname']
    del d['version']
    del d['fqname']
    del d['cache_key']
    ds = self.database.new_dataset(**d)
    nb = self.bundle(ds.vid)
    nb.set_file_system(source_url=b.source_fs.getsyspath('/'))
    nb.state = Bundle.STATES.NEW
    nb.commit()
    for f in b.dataset.files:
        assert f.major_type == f.MAJOR_TYPE.BUILDSOURCE
        nb.dataset.files.append(nb.dataset.bsfile(f.minor_type, f.path).
            update(f))
    nb.build_source_files.file(File.BSFILE.META).record_to_objects()
    nb.build_source_files.file(File.BSFILE.META).objects_to_record()
    ds.commit()
    return nb