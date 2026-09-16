def hl_table2canvas(self, w, res_dict):
    objlist = []
    if self.maskhltag:
        try:
            self.canvas.delete_object_by_tag(self.maskhltag, redraw=False)
        except Exception:
            pass
    for sub_dict in res_dict.values():
        for seqno in sub_dict:
            mobj = self._maskobjs[int(seqno) - 1]
            dat = self._rgbtomask(mobj)
            obj = self.dc.Image(0, 0, masktorgb(dat, color=self.hlcolor,
                alpha=self.hlalpha))
            objlist.append(obj)
    if len(objlist) > 0:
        self.maskhltag = self.canvas.add(self.dc.CompoundObject(*objlist))
    self.fitsimage.redraw()