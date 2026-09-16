def get_evernote_notes(self, evernote_filter):
    data = []
    note_store = self.client.get_note_store()
    our_note_list = note_store.findNotesMetadata(self.token,
        evernote_filter, 0, 100, EvernoteMgr.set_evernote_spec())
    for note in our_note_list.notes:
        whole_note = note_store.getNote(self.token, note.guid, True, True,
            False, False)
        content = self._cleaning_content(whole_note.content)
        data.append({'title': note.title, 'my_date': arrow.get(note.created
            ), 'link': whole_note.attributes.sourceURL, 'content': content})
    return data