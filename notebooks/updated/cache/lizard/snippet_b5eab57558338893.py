def mousePressEvent(self, event):
    if not self.scene:
        return
    if self.event_sel or self.current_event:
        self.parent.notes.idx_eventtype.setCurrentText(self.current_etype)
        self.current_etype = None
        self.current_event = None
        self.deselect = True
        self.event_sel = None
        self.current_event_row = None
        self.scene.removeItem(self.highlight)
        self.highlight = None
        self.parent.statusBar().showMessage('')
        return
    self.ready = False
    self.event_sel = None
    xy_scene = self.mapToScene(event.pos())
    chan_idx = argmin(abs(asarray(self.chan_pos) - xy_scene.y()))
    self.sel_chan = chan_idx
    self.sel_xy = xy_scene.x(), xy_scene.y()
    chk_marker = self.parent.notes.action['new_bookmark'].isChecked()
    chk_event = self.parent.notes.action['new_event'].isChecked()
    if not (chk_marker or chk_event):
        channame = self.chan[self.sel_chan] + ' in selected window'
        self.parent.spectrum.show_channame(channame)
    else:
        for annot in self.idx_annot:
            if annot.contains(xy_scene):
                self.highlight_event(annot)
                if chk_event:
                    row = self.parent.notes.find_row(annot.marker.x(), 
                        annot.marker.x() + annot.marker.width())
                    self.parent.notes.idx_annot_list.setCurrentCell(row, 0)
                break
    self.ready = True