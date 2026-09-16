def on_receive_append_entries(self, data):
    if self.storage.term == data['term']:
        self.state.to_follower()