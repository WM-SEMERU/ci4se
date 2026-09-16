def enrollments(db, uuid=None, organization=None, from_date=None, to_date=None
    ):
    if not from_date:
        from_date = MIN_PERIOD_DATE
    if not to_date:
        to_date = MAX_PERIOD_DATE
    if from_date < MIN_PERIOD_DATE or from_date > MAX_PERIOD_DATE:
        raise InvalidValueError("'from_date' %s is out of bounds" % str(
            from_date))
    if to_date < MIN_PERIOD_DATE or to_date > MAX_PERIOD_DATE:
        raise InvalidValueError("'to_date' %s is out of bounds" % str(to_date))
    if from_date and to_date and from_date > to_date:
        raise InvalidValueError("'from_date' %s cannot be greater than %s" %
            (from_date, to_date))
    enrollments = []
    with db.connect() as session:
        query = session.query(Enrollment).join(UniqueIdentity, Organization
            ).filter(Enrollment.start >= from_date, Enrollment.end <= to_date)
        if uuid:
            uidentity = find_unique_identity(session, uuid)
            if not uidentity:
                raise NotFoundError(entity=uuid)
            query = query.filter(Enrollment.uidentity == uidentity)
        if organization:
            org = find_organization(session, organization)
            if not org:
                raise NotFoundError(entity=organization)
            query = query.filter(Enrollment.organization == org)
        enrollments = query.order_by(UniqueIdentity.uuid, Organization.name,
            Enrollment.start, Enrollment.end).all()
        session.expunge_all()
    return enrollments