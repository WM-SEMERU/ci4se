def default_node(self, value):
    if value is not None:
        assert issubclass(value, AbstractCompositeNode
            ), "'{0}' attribute: '{1}' is not a '{2}' subclass!".format(
            'default_node', value, AbstractCompositeNode.__name__)
    self.__default_node = value