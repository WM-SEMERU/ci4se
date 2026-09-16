def find_selected(self, event):
    for i in range(len(self.items)):
        m = self.items[i]
        ret = m.find_selected(event)
        if ret is not None:
            return ret
    return None