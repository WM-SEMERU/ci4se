def delete_unused_subjects():
    query = d1_gmn.app.models.Subject.objects.all()
    query = query.filter(scienceobject_submitter__isnull=True)
    query = query.filter(scienceobject_rights_holder__isnull=True)
    query = query.filter(eventlog__isnull=True)
    query = query.filter(permission__isnull=True)
    query = query.filter(whitelistforcreateupdatedelete__isnull=True)
    logger.debug('Deleting {} unused subjects:'.format(query.count()))
    for s in query.all():
        logging.debug('  {}'.format(s.subject))
    query.delete()