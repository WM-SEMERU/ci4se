def on_click_search_widget(self, event):
    self.search.cats = self.cats
    self.search.visible = event.new
    if self.search.visible:
        self.search.watchers.append(self.select.widget.link(self.search,
            value='cats'))