def create_widget(self):
    d = self.declaration
    if d.orientation == 'vertical':
        self.widget = ScrollView(self.get_context(), None, d.style)
    else:
        self.widget = HorizontalScrollView(self.get_context(), None, d.style)