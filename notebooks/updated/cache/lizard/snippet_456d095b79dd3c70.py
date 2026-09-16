def get_group_hidden(self):
    for element in self.group_list:
        if element.form.view_type != 'none':
            return False
        for child_element in element.children:
            if child_element.form.view_type != 'none':
                return False
    return True