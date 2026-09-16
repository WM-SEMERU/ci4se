def get_collections_like_name(collection_name, **kwargs):
    try:
        collections = db.DBSession.query(DatasetCollection).filter(
            DatasetCollection.name.like('%%%s%%' % collection_name.lower())
            ).all()
    except NoResultFound:
        raise ResourceNotFoundError(
            'No dataset collection found with name %s' % collection_name)
    return collections