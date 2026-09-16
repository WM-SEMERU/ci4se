def build_flex_args_keys(components):

    def _prepend_first(components, sub_components):
        ret = []
        for first in components[0]:
            for sub_component in sub_components:
                ret.append('{}.{}'.format(first, sub_component))
        return ret
    if len(components) > 1:
        sub_components = build_flex_args_keys(components[1:])
        return _prepend_first(components, sub_components)
    if len(components) == 1:
        return components[0]
    return []