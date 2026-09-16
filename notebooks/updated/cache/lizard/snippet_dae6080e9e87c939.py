def change_size_for_active_pane(self, up=0, right=0, down=0, left=0):
    child = self.active_pane
    self.change_size_for_pane(child, up=up, right=right, down=down, left=left)