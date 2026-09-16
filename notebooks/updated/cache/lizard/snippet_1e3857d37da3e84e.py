def oaiset(self):
    if current_app.config['COMMUNITIES_OAI_ENABLED']:
        from invenio_oaiserver.models import OAISet
        return OAISet.query.filter_by(spec=self.oaiset_spec).one()
    else:
        return None