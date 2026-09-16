def do_mo(self):
    log.debug('Start updating mo files ...')
    for po_dir_path in self._iter_po_dir():
        po_path = (po_dir_path / self._basename).with_suffix('.po')
        lc_path = self._mo_path / po_dir_path.name / 'LC_MESSAGES'
        lc_path.mkdir(parents=True, exist_ok=True)
        mo_path = (lc_path / self._basename).with_suffix('.mo')
        log.debug('Creating from {po}: {mo}'.format(po=str(po_path), mo=str
            (mo_path)))
        check_call(['msgfmt', str(po_path), '-o', str(mo_path)])
    log.debug('All mo files updated')