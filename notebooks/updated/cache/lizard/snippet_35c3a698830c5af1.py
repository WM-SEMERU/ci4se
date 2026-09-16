def marvcli_discard(datasets, all_nodes, nodes, tags, comments, confirm):
    mark_discarded = not any([all_nodes, nodes, tags, comments])
    site = create_app().site
    setids = parse_setids(datasets)
    if tags or comments:
        if confirm:
            msg = ' and '.join(filter(None, ['tags' if tags else None, 
                'comments' if comments else None]))
            click.echo('About to delete {}'.format(msg))
            click.confirm('This cannot be undone. Do you want to continue?',
                abort=True)
        ids = [x[0] for x in db.session.query(Dataset.id).filter(Dataset.
            setid.in_(setids))]
        if tags:
            where = dataset_tag.c.dataset_id.in_(ids)
            stmt = dataset_tag.delete().where(where)
            db.session.execute(stmt)
        if comments:
            comment_table = Comment.__table__
            where = comment_table.c.dataset_id.in_(ids)
            stmt = comment_table.delete().where(where)
            db.session.execute(stmt)
    if nodes or all_nodes:
        storedir = site.config.marv.storedir
        for setid in setids:
            setdir = os.path.join(storedir, setid)
    if mark_discarded:
        dataset = Dataset.__table__
        stmt = dataset.update().where(dataset.c.setid.in_(setids)).values(
            discarded=True)
        db.session.execute(stmt)
    db.session.commit()