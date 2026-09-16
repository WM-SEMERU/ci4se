def parse_section(self, section_options):
    for name, (_, value) in section_options.items():
        try:
            self[name] = value
        except KeyError:
            pass