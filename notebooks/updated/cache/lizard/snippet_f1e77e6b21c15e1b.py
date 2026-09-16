def denormalized(self):
    with self.locker:
        self._update_meta()
        output = [{'table': c.es_index, 'name': untype_path(c.name),
            'cardinality': c.cardinality, 'es_column': c.es_column,
            'es_index': c.es_index, 'last_updated': c.last_updated, 'count':
            c.count, 'nested_path': [unnest_path(n) for n in c.nested_path],
            'es_type': c.es_type, 'type': c.jx_type} for tname, css in self
            .data.items() for cname, cs in css.items() for c in cs if c.
            jx_type not in STRUCT]
    from jx_python.containers.list_usingPythonList import ListContainer
    return ListContainer(self.name, data=output, schema=jx_base.Schema(
        'meta.columns', SIMPLE_METADATA_COLUMNS))