def _load_section(self, lines, section):
    members = []
    while True:
        if len(lines) == 0:
            break
        next_line = lines[0]
        if next_line.strip().startswith('%'):
            break
        else:
            new_member = lines.pop(0).strip()
            if new_member not in ['', None]:
                members.append(new_member)
    if len(members) > 0:
        if section is not None:
            self.config[section] += members