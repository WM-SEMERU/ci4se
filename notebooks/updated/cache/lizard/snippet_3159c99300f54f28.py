def OnMarginClick(self, evt):
    if evt.GetMargin() == 2:
        if evt.GetShift() and evt.GetControl():
            self.fold_all()
        else:
            line_clicked = self.LineFromPosition(evt.GetPosition())
            if self.GetFoldLevel(line_clicked) & stc.STC_FOLDLEVELHEADERFLAG:
                if evt.GetShift():
                    self.SetFoldExpanded(line_clicked, True)
                    self.expand(line_clicked, True, True, 1)
                elif evt.GetControl():
                    if self.GetFoldExpanded(line_clicked):
                        self.SetFoldExpanded(line_clicked, False)
                        self.expand(line_clicked, False, True, 0)
                    else:
                        self.SetFoldExpanded(line_clicked, True)
                        self.expand(line_clicked, True, True, 100)
                else:
                    self.ToggleFold(line_clicked)