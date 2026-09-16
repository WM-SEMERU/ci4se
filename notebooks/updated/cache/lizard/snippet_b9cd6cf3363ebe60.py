def build_row_dict(cls, row, dialect, deleted=False, user_id=None,
    use_dirty=True):
    data = {'data': row.to_archivable_dict(dialect, use_dirty=use_dirty),
        'deleted': deleted, 'updated_at': datetime.now(), 'version_id': 
        current_version_sql(as_is=True) if deleted else row.version_id}
    for col_name in row.version_columns:
        data[col_name] = utils.get_column_attribute(row, col_name,
            use_dirty=use_dirty)
    if user_id is not None:
        data['user_id'] = user_id
    return data