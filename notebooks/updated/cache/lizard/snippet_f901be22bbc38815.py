def chooseForm_slot(self, element, element_old):
    self.current_slot = None
    if verbose:
        print(self.pre, 'chooseForm_slot :', element)
    if isinstance(element, type(None)):
        self.current_row = None
        self.element = None
    else:
        assert hasattr(element, '_id')
        assert hasattr(element, 'classname')
        try:
            self.current_row = self.row_instance_by_name[element.classname]
        except KeyError:
            print(self.pre,
                'chooseForm_slot : no such classname for this FormSet : ',
                element.classname)
            self.current_row = None
            self.element = None
        else:
            self.resetForm()
            self.current_row.get(self.collection, element._id)
            self.element = element
            self.current_slot = self.current_row.get_column_value('slot')
    self.showCurrent()