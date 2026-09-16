def delete_show_function(self, show_name):
    if self.get_show_function(show_name) is None:
        return
    self.shows.__delitem__(show_name)