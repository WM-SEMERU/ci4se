def _block_width(self):
    section = self.sections[-1]
    return Emu(section.page_width - section.left_margin - section.right_margin)