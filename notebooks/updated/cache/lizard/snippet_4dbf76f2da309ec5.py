def delete_dataset(dataset_id, **kwargs):
    try:
        d = db.DBSession.query(Dataset).filter(Dataset.id == dataset_id).one()
    except NoResultFound:
        raise HydraError('Dataset %s does not exist.' % dataset_id)
    dataset_rs = db.DBSession.query(ResourceScenario).filter(
        ResourceScenario.dataset_id == dataset_id).all()
    if len(dataset_rs) > 0:
        raise HydraError(
            'Cannot delete %s. Dataset is used by one or more resource scenarios.'
             % dataset_id)
    db.DBSession.delete(d)
    db.DBSession.flush()
    db.DBSession.expunge_all()