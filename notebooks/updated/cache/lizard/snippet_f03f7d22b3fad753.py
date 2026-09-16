def _new_output_char(self, char):
    self.text.config(state=tkinter.NORMAL)
    self.text.insert('end', char)
    self.text.see('end')
    self.text.config(state=tkinter.DISABLED)