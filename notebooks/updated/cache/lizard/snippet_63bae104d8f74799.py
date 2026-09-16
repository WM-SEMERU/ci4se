def _rpt_unused_sections(self, prt):
    sections_unused = set(self.sections_seen).difference(self.section2goids
        .keys())
    for sec in sections_unused:
        prt.write('  UNUSED SECTION: {SEC}\n'.format(SEC=sec))