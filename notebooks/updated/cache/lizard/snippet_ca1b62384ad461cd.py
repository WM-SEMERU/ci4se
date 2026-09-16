def seq_view_shot(self):
    if not self.cur_seq:
        return
    i = self.seq_shot_tablev.currentIndex()
    item = i.internalPointer()
    if item:
        shot = item.internal_data()
        self.view_shot(shot)