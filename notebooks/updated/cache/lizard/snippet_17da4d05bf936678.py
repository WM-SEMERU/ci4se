def print_summary(self):
    for input in self.form.find_all(('input', 'textarea', 'select', 'button')):
        input_copy = copy.copy(input)
        for subtag in (input_copy.find_all() + [input_copy]):
            if subtag.string:
                subtag.string = subtag.string.strip()
        print(input_copy)