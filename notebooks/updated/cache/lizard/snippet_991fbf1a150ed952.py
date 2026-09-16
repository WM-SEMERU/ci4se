def get_default_name(self):
    long_names = [name for name in self.name if name.startswith('--')]
    short_names = [name for name in self.name if not name.startswith('--')]
    if long_names:
        return to_snake_case(long_names[0].lstrip('-'))
    return to_snake_case(short_names[0].lstrip('-'))