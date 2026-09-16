def split_multi_sections(self):
    for section in self.sections():
        if '&' not in section:
            continue
        splitSections = section.split('&')
        for newSec in splitSections:
            if not self.has_section(newSec):
                self.add_section(newSec)
            self.add_options_to_section(newSec, self.items(section))
        self.remove_section(section)