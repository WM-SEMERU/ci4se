def find(expression, schema=None):
    parser = SchemaFreeParser() if schema is None else SchemaAwareParser(schema
        )
    return parser.parse(expression)