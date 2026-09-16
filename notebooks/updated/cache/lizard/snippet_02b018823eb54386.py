def errors_as_text(self):
    errors = []
    errors.append(self.non_field_errors().as_text())
    errors_data = self.errors.as_data()
    for key, value in errors_data.items():
        field_label = self.fields[key].label
        err_descn = ''.join([force_text(e.message) for e in value])
        error = '%s %s' % (field_label, err_descn)
        errors.append(error)
    return ','.join(errors)