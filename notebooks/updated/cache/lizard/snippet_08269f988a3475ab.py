def _parse_lines(self, f, chunk, db_type, celery_obj=False, c=0):
    old = 0
    for i, line in enumerate(f):
        line = line.rstrip()
        if i == 0:
            old = self.current_id_meta
        self._update_libdata(line)
        if self.current_id_meta > old:
            old = self.current_id_meta
            c += 1
        if c > chunk:
            if celery_obj:
                celery_obj.update_state(state='current spectra {}'.format(
                    str(i)), meta={'current': i, 'total': self.num_lines})
            print(self.current_id_meta)
            self.insert_data(remove_data=True, db_type=db_type)
            self.update_source = False
            c = 0
    return c