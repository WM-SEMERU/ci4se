def data_from_stream(self, stream):
    parser = self._make_representation_parser(stream, self.resource_class,
        self._mapping)
    return parser.run()