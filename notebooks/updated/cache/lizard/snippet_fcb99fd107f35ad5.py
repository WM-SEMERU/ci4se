def validate_is_non_abstract_vertex_type(self, vertex_classname):
    element = self.get_vertex_schema_element_or_raise(vertex_classname)
    if element.abstract:
        raise InvalidClassError(
            'Expected a non-abstract vertex class, but {} is abstract'.
            format(vertex_classname))