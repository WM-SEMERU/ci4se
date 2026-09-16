def populate_shared_sections(self):
    if not self.has_section('sharedoptions'):
        return
    for key, value in self.items('sharedoptions'):
        assert self.has_section('sharedoptions-%s' % key)
        values = value.split(',')
        common_options = self.items('sharedoptions-%s' % key)
        for section in values:
            if not self.has_section(section):
                self.add_section(section)
            for arg, val in common_options:
                if arg in self.options(section):
                    raise ValueError('Option exists in both original ' + 
                        'ConfigParser section [%s] and ' % (section,) + 
                        'sharedoptions section: %s %s' % (arg, 
                        'sharedoptions-%s' % key))
                self.set(section, arg, val)
        self.remove_section('sharedoptions-%s' % key)
    self.remove_section('sharedoptions')