def add_private_note(self, private_notes, source=None):
    self._append_to('_private_notes', self._sourced_dict(source, value=
        private_notes))