def collect(self, top, sup, argv=None, parent=''):
    try:
        namespace, tag = _namespace_and_tag(self, self.ref, top)
        try:
            if self.xmlns_map[namespace] == top.target_namespace:
                cti = get_type_def(tag, top.parts)
                try:
                    return cti.py_class.properties
                except ValueError:
                    return cti.collect(top, sup)
            else:
                raise Exception(
                    'Reference to group in other XSD file, not supported')
        except KeyError:
            raise Exception('Missing namespace definition')
    except AttributeError as exc:
        print('#!!!!', exc)
        return [], []