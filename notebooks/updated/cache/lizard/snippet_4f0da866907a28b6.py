def update(self, data, make_backup=True, **kwargs):
    from gffutils import create
    from gffutils import iterators
    if make_backup:
        if isinstance(self.dbfn, six.string_types):
            shutil.copy2(self.dbfn, self.dbfn + '.bak')
    _iterator_kwargs = {}
    for k, v in kwargs.items():
        if k in constants._iterator_kwargs:
            _iterator_kwargs[k] = v
    data = iterators.DataIterator(data, **_iterator_kwargs)
    if self.dialect['fmt'] == 'gtf':
        if 'id_spec' not in kwargs:
            kwargs['id_spec'] = {'gene': 'gene_id', 'transcript':
                'transcript_id'}
        db = create._GTFDBCreator(data=data, dbfn=self.dbfn, dialect=self.
            dialect, **kwargs)
    elif self.dialect['fmt'] == 'gff3':
        if 'id_spec' not in kwargs:
            kwargs['id_spec'] = 'ID'
        db = create._GFFDBCreator(data=data, dbfn=self.dbfn, dialect=self.
            dialect, **kwargs)
    else:
        raise ValueError
    db._populate_from_lines(data)
    db._update_relations()
    db._finalize()
    return db