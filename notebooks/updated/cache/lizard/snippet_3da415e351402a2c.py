def create_widget(self):
    d = self.declaration
    self.widget = RelativeLayout(self.get_context(), None, d.style)