def get_details(self):
    if isinstance(self.validation_outcome, Exception):
        prefix = ('Validation function [{val}] raised ' if self.
            display_prefix_for_exc_outcomes else '')
        contents = ('Error validating {what}. ' + prefix +
            '{exception}: {details}').format(what=self.get_what_txt(), val=
            self.validator.get_main_function_name(), exception=type(self.
            validation_outcome).__name__, details=end_with_dot(str(self.
            validation_outcome)))
    else:
        contents = (
            'Error validating {what}: validation function [{val}] returned [{result}].'
            .format(what=self.get_what_txt(), val=self.validator.
            get_main_function_name(), result=self.validation_outcome))
    return contents