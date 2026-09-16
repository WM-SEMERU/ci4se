def delete(ids, force):
    records_deprecation_warning()
    from .api import Record
    for id_ in ids:
        record = Record.get_record(id_, with_deleted=force)
        record.delete(force=force)
    db.session.commit()