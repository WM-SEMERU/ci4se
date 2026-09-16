def on_tab_close_clicked(self, event, state_m):
    [page, state_identifier] = self.find_page_of_state_m(state_m)
    if page:
        self.close_page(state_identifier, delete=False)