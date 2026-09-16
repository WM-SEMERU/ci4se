def _init_journal(self, permissive=True):
    nowstamp = datetime.now().strftime('%d-%b-%Y %H:%M:%S.%f')[:-3]
    self._add_entry(templates.INIT.format(time_stamp=nowstamp))
    if permissive:
        self._add_entry(templates.INIT_DEBUG)