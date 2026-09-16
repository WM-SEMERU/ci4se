def add_line(self, line):
    if not self.is_valid_line(line):
        logger.warn("Invalid line for %s section: '%s'", self.section_name,
            line)
        return
    self.lines.append(line)