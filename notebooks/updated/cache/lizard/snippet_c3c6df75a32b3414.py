def generic_is_view_attribute(parents, attrs):

    def is_attribute(node):
        return _attribute_is_magic(node, attrs, parents)
    return is_attribute