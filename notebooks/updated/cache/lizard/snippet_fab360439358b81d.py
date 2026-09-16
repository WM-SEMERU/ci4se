def get_initial(self):
    initial = super(MultiFormView, self).get_initial()
    for key in six.iterkeys(self.form_classes):
        initial[key] = {}
    return initial