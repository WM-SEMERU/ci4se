def skip(self):
    for pos, element in self.element_iter:
        tag, class_attr = _tag_and_class_attr(element)
        if tag == 'div' and 'thread' in class_attr and pos == 'end':
            break