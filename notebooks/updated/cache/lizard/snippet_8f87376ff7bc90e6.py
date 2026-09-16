def get_methods(self):
    return [('levels', self.print_levels), ('make', self.make_report), (
        'clear', self.clear_report), ('show', self.show_report), ('write',
        self.write_report)]