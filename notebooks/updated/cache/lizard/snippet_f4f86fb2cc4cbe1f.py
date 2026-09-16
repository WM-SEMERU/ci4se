def _render_pages(self):
    self.style_log = StyleLog(self.stylesheet)
    self.floats = set()
    self.placed_footnotes = set()
    self._start_time = time.time()
    part_page_counts = {}
    part_page_count = PartPageCount()
    last_number_format = None
    for part_template in self.part_templates:
        part = part_template.document_part(self, part_page_count.count + 1)
        if part is None:
            continue
        if part_template.page_number_format != last_number_format:
            part_page_count = PartPageCount()
        part_page_count += part.render(part_page_count.count + 1)
        part_page_counts[part_template.name] = part_page_count
        last_number_format = part_template.page_number_format
    sys.stdout.write('\n')
    return part_page_counts