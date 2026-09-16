def refresh(self):
    self._update_id_list()
    for _id in self.history[:]:
        if _id not in self.id_list:
            self.history.remove(_id)