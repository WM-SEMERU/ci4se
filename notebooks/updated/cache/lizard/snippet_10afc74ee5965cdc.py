def get_dataset(dataset_id, **kwargs):
    user_id = int(kwargs.get('user_id'))
    if dataset_id is None:
        return None
    try:
        dataset_rs = db.DBSession.query(Dataset.id, Dataset.type, Dataset.
            unit_id, Dataset.name, Dataset.hidden, Dataset.cr_date, Dataset
            .created_by, DatasetOwner.user_id, null().label('metadata'),
            case([(and_(Dataset.hidden == 'Y', DatasetOwner.user_id is not
            None), None)], else_=Dataset.value).label('value')).filter(
            Dataset.id == dataset_id).outerjoin(DatasetOwner, and_(
            DatasetOwner.dataset_id == Dataset.id, DatasetOwner.user_id ==
            user_id)).one()
        rs_dict = dataset_rs._asdict()
        if dataset_rs.value is not None:
            rs_dict['value'] = str(dataset_rs.value)
        if (dataset_rs.hidden == 'N' or dataset_rs.hidden == 'Y' and 
            dataset_rs.user_id is not None):
            metadata = db.DBSession.query(Metadata).filter(Metadata.
                dataset_id == dataset_id).all()
            rs_dict['metadata'] = metadata
        else:
            rs_dict['metadata'] = []
    except NoResultFound:
        raise HydraError('Dataset %s does not exist.' % dataset_id)
    dataset = namedtuple('Dataset', rs_dict.keys())(**rs_dict)
    return dataset