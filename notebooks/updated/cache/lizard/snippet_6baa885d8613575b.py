def get_section2usrnts(self):
    sec_nts = []
    for section_name, _ in self.get_sections_2d():
        usrgos = self.get_usrgos_g_section(section_name)
        sec_nts.append((section_name, [self.go2nt.get(u) for u in usrgos]))
    return cx.OrderedDict(sec_nts)