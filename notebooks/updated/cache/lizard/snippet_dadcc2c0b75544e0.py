def update(self, event=None, force=False):
    line_no = self.text.index(tkinter.INSERT).split('.')[0]
    self.text.tag_remove(self.tag_current_line.id, '1.0', 'end')
    self.text.tag_add(self.tag_current_line.id, '%s.0' % line_no, 
        '%s.0+1lines' % line_no)