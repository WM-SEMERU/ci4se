def generate_html(self, jdoc, schema, schemas):
    params = {'functions': sorted([j for j in jdoc if j.schema_name ==
        schema.object_name and j.object_type in ['function', 'procedure',
        'trigger']], key=lambda x: x.object_name), 'tables': sorted([j for
        j in jdoc if j.schema_name == schema.object_name and j.object_type in
        ['table', 'view', 'materialized view', 'foreign table']], key=lambda
        x: x.object_name), 'schema_name': schema.object_name, 'schemas':
        sorted(schemas, key=lambda x: x.object_name), 'project': self.
        project_name, 'title': '{}: schema {}'.format(self.project_name,
        schema.object_name)}
    template = self.lookup.get_template('schema.mako')
    html = template.render_unicode(**params)
    return html