def reference_handler(self, iobject, fact, attr_info, add_fact_kargs):
    namespace_uri, uid = self.identifier_ns_uri, attr_info['idref']
    timestamp = attr_info['@timestamp']
    target_mantis_obj, existed = MantisImporter.create_iobject(uid=uid,
        identifier_ns_uri=namespace_uri, timestamp=timestamp)
    logger.debug('Creation of Placeholder for %s %s returned %s' % (
        namespace_uri, uid, existed))
    add_fact_kargs['value_iobject_id'] = Identifier.objects.get(uid=uid,
        namespace__uri=namespace_uri)
    return True