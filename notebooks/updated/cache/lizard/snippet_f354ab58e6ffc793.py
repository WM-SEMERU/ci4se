def parse(self):
    for line in self.lines:
        field_defs = self.parse_line(line)
        fields = []
        for kind, options in field_defs:
            logger.debug('Creating field %s(%r)', kind, options)
            fields.append(self.field_registry.create(kind, **options))
        self.line_fields.append(fields)
        for field in fields:
            self.widgets[field] = None