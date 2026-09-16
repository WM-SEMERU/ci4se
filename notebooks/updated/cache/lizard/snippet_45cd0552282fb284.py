def update_label(self, old_label, new_label, callback=dummy_progress_cb):
    current = 0
    total = self.index.get_nb_docs()
    self.index.start_update_label(old_label, new_label)
    while True:
        op, doc = self.index.continue_update_label()
        if op == 'end':
            break
        callback(current, total, self.LABEL_STEP_UPDATING, doc)
        current += 1
    self.index.end_update_label()