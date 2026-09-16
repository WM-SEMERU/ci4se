def destroy_oaipmh_set(mapper, connection, community):
    from invenio_oaiserver.models import OAISet
    with db.session.begin_nested():
        oaiset = OAISet.query.filter_by(spec=community.oaiset_spec
            ).one_or_none()
        if oaiset is None:
            raise Exception('OAISet for community {0} is missing'.format(
                community.id))
        db.session.delete(oaiset)