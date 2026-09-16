def append_child_field(self, linenum, indent, field_name, field_value):
    frame = self.current_frame()
    assert isinstance(frame, RootFrame) or isinstance(frame, ContainerFrame
        ) and frame.indent < indent
    if frame.container.contains(ROOT_PATH, field_name):
        raise KeyError('field {0} exists in container at path {1}'.format(
            field_name, frame.path))
    frame.container.put_field(ROOT_PATH, field_name, field_value)
    frame = FieldFrame(linenum, indent, frame.path, frame.container,
        field_name, field_value)
    self.push_frame(frame)