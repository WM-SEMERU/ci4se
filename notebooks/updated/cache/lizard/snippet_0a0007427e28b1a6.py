def update_dimension(dimension, **kwargs):
    db_dimension = None
    dimension = JSONObject(dimension)
    try:
        db_dimension = db.DBSession.query(Dimension).filter(Dimension.id ==
            dimension.id).filter().one()
        if 'description' in dimension and dimension['description'] is not None:
            db_dimension.description = dimension['description']
        if 'project_id' in dimension and dimension['project_id'
            ] is not None and dimension['project_id'] != '' and dimension[
            'project_id'].isdigit():
            db_dimension.project_id = dimension['project_id']
    except NoResultFound:
        raise ResourceNotFoundError('Dimension (ID=%s) does not exist' %
            dimension.id)
    db.DBSession.flush()
    return JSONObject(db_dimension)