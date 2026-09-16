def create_widget(self):
    d = self.declaration
    self.widget = View(self.get_context(), None, d.style)