def _need_bib_run(self, old_cite_counter):
    with open('%s.aux' % self.project_name) as fobj:
        match = BIB_PATTERN.search(fobj.read())
        if not match:
            return False
        else:
            self.bib_file = match.group(1)
    if not os.path.isfile('%s.bib' % self.bib_file):
        self.log.warning('Could not find *.bib file.')
        return False
    if re.search('No file %s.bbl.' % self.project_name, self.out) or re.search(
        'LaTeX Warning: Citation .* undefined', self.out):
        return True
    if old_cite_counter != self.generate_citation_counter():
        return True
    if os.path.isfile('%s.bib.old' % self.bib_file):
        new = '%s.bib' % self.bib_file
        old = '%s.bib.old' % self.bib_file
        if not filecmp.cmp(new, old):
            return True