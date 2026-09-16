def destroy(self):
    if self.master is not None:
        self.master._remove_child(self)
    self.tk.destroy()