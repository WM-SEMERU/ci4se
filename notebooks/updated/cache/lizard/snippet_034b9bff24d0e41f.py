def handle_update_search_space(self, data):
    self.searchspace_json = data
    self.random_state = np.random.RandomState()