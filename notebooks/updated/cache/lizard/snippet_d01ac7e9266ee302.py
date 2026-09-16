def _create_orchestrated_cat(self, foreign_catalog_id, db_name, cat_name):
    if (foreign_catalog_id.identifier_namespace == db_name + '.' + cat_name and
        foreign_catalog_id.authority == self._authority):
        raise errors.NotFound()
    foreign_service_name = foreign_catalog_id.get_identifier_namespace().split(
        '.')[0]
    catalog_name = camel_to_under(foreign_catalog_id.namespace.split('.')[1])
    manager = self._get_provider_manager(foreign_service_name.upper())
    lookup_session = getattr(manager, 'get_{0}_lookup_session'.format(
        catalog_name))(proxy=self._proxy)
    getattr(lookup_session, 'get_{0}'.format(catalog_name))(foreign_catalog_id)
    collection = JSONClientValidated(db_name, collection=cat_name, runtime=
        self._runtime)
    foreign_identifier = ObjectId(foreign_catalog_id.get_identifier())
    default_text = 'Orchestrated ' + foreign_service_name
    catalog_map = make_catalog_map(cat_name, identifier=foreign_identifier,
        default_text=default_text)
    collection.insert_one(catalog_map)
    alias_id = Id(identifier=foreign_catalog_id.identifier, namespace=
        db_name + '.' + cat_name, authority=self._authority)
    try:
        admin_session = getattr(manager, 'get_{0}_admin_session'.format(
            catalog_name))(proxy=self._proxy)
        getattr(admin_session, 'alias_{0}'.format(catalog_name))(
            foreign_catalog_id, alias_id)
    except (errors.Unimplemented, AttributeError):
        pass
    return catalog_map