def data_element_tree_to_string(data_element):

    def __dump(data_el, stream, offset):
        name = data_el.__class__.__name__
        stream.write('%s%s' % (' ' * offset, name))
        offset += 2
        ifcs = provided_by(data_el)
        if ICollectionDataElement in ifcs:
            stream.write('[')
            first_member = True
            for member_data_el in data_el.get_members():
                if first_member:
                    stream.write('%s' % os.linesep + ' ' * offset)
                    first_member = False
                else:
                    stream.write(',%s' % os.linesep + ' ' * offset)
                __dump(member_data_el, stream, offset)
            stream.write(']')
        else:
            stream.write('(')
            if ILinkedDataElement in ifcs:
                stream.write('url=%s, kind=%s, relation=%s' % (data_el.
                    get_url(), data_el.get_kind(), data_el.get_relation()))
            else:
                first_attr = True
                for attr_name, attr_value in iteritems_(data_el.data):
                    if first_attr:
                        first_attr = False
                    else:
                        stream.write(',%s' % os.linesep + ' ' * (offset +
                            len(name) + 1))
                    if attr_value is None:
                        continue
                    if not IResourceDataElement in provided_by(attr_value):
                        stream.write('%s=%s' % (attr_name, attr_value))
                    else:
                        stream.write('%s=' % attr_name)
                        __dump(attr_value, stream, offset)
            stream.write(')')
    stream = NativeIO()
    __dump(data_element, stream, 0)
    return stream.getvalue()