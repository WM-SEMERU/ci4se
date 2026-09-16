def _read_finish(self, goids_fin, prt):
    if len(self.section2goids) != len(self.sections_seen):
        self._rpt_unused_sections(prt)
    if not self.sections_seen:
        self.goids_fin = goids_fin
    if goids_fin:
        return self.internal_get_goids_or_sections()
    else:
        sys.stdout.write(
            '\n**WARNING: GO IDs MUST BE THE FIRST 10 CHARACTERS OF EACH LINE\n\n'
            )