def reset(self):
    for i in range(len(self.values)):
        self.values[i].delete(0, tk.END)
        if self.defaults[i] is not None:
            self.values[i].insert(0, self.defaults[i])