def _add_notes_slide_part(self):
    notes_slide_part = NotesSlidePart.new(self.package, self)
    self.relate_to(notes_slide_part, RT.NOTES_SLIDE)
    return notes_slide_part