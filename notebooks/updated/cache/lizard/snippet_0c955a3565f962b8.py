def select(self, template_name):
    return [fam for fam in self.families if fam.template.name == template_name
        ][0]