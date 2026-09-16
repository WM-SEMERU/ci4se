def get_default_classes(self):
    if not self.url:
        self.column.classes = [cls for cls in self.column.classes if cls !=
            'anchor']
    column_class_string = self.column.get_final_attrs().get('class', '')
    classes = set(column_class_string.split(' '))
    if self.column.status:
        classes.add(self.get_status_class(self.status))
    if self.inline_edit_available:
        classes.add('inline_edit_available')
    return list(classes)