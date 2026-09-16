def load_recipe(self):
    lines = self.lines.copy()
    comments = []
    self.config = dict()
    section = None
    name = None
    while len(lines) > 0:
        line = lines.pop(0)
        stripped = line.strip()
        if re.search('(b|B)(o|O){2}(t|T)(s|S)(t|T)(r|R)(a|A)(p|P)', line):
            self._load_bootstrap(stripped)
        if re.search('(f|F)(r|R)(O|o)(m|M)', stripped):
            self._load_from(stripped)
        if stripped.startswith('#'):
            comments.append(stripped)
            continue
        elif stripped.startswith('%'):
            section = self._add_section(stripped)
            bot.debug('Adding section title %s' % section)
        elif section is not None:
            lines = [line] + lines
            self._load_section(lines=lines, section=section)
        self.config['comments'] = comments