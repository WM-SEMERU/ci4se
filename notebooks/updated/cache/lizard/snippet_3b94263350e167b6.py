def descriptor_factory(self, type_name, shard='lobby', **kwargs):
    desc = factories.build(type_name, shard=unicode(shard), **kwargs)
    return self._database_connection.save_document(desc)