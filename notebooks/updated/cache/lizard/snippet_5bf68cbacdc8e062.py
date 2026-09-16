def get_meta_attributes(self, **kwargs):
    superuser = kwargs.get('superuser', False)
    if (self.untl_object.qualifier == 'recordStatus' or self.untl_object.
        qualifier == 'system'):
        if superuser:
            self.editable = True
            self.repeatable = True
        else:
            self.editable = False
        self.view_type = 'qualified-input'
    elif self.untl_object.qualifier == 'hidden':
        self.label = 'Object Hidden'
        self.view_type = 'radio'
    else:
        self.editable = False
        self.view_type = 'qualified-input'