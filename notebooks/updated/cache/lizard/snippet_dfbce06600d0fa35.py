def is_valid_line(self, line):
    adjusted_line = line.strip().lower()
    return any([adjusted_line.startswith(directive) for directive in
        directives_by_section[self.section_name]])