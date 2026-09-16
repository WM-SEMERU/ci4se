def get_perm(perm_id, **kwargs):
    try:
        perm = db.DBSession.query(Perm).filter(Perm.id == perm_id).one()
        return perm
    except NoResultFound:
        raise ResourceNotFoundError('Permission not found (perm_id={})'.
            format(perm_id))