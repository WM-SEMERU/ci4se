def close_all_pages(self):
    states_to_be_closed = []
    for state_identifier in self.tabs:
        states_to_be_closed.append(state_identifier)
    for state_identifier in states_to_be_closed:
        self.close_page(state_identifier, delete=False)