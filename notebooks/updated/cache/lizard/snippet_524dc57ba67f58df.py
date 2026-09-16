def buffer_typechecks(self, call_id, payload):
    if self.currently_buffering_typechecks:
        for note in payload['notes']:
            self.buffered_notes.append(note)