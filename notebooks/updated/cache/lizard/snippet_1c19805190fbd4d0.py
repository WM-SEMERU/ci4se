def insert_text(self, data, overwrite=False, move_cursor=True, fire_event=True
    ):
    otext = self.text
    ocpos = self.cursor_position
    if overwrite:
        overwritten_text = otext[ocpos:ocpos + len(data)]
        if '\n' in overwritten_text:
            overwritten_text = overwritten_text[:overwritten_text.find('\n')]
        self.text = otext[:ocpos] + data + otext[ocpos + len(overwritten_text):
            ]
    else:
        self.text = otext[:ocpos] + data + otext[ocpos:]
    if move_cursor:
        self.cursor_position += len(data)
    if fire_event:
        self.on_text_insert.fire()