def get_pos_in_delegate(self, index, globalpos):
    rect = self.visualRect(index)
    p = self.viewport().mapToGlobal(rect.topLeft())
    return globalpos - p