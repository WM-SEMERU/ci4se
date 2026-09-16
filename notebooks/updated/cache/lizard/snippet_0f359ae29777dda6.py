def path_placeholders(self):
    parser = string.Formatter()
    return [placeholder_name for _, placeholder_name, _, _ in parser.parse(
        self.path) if placeholder_name]