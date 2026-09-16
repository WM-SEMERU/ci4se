def OnSearch(self, event):
    search_string = self.search.GetValue()
    if search_string not in self.search_history:
        self.search_history.append(search_string)
    if len(self.search_history) > 10:
        self.search_history.pop(0)
    self.menu = self.make_menu()
    self.search.SetMenu(self.menu)
    search_flags = self.search_options + ['FIND_NEXT']
    post_command_event(self, self.FindMsg, text=search_string, flags=
        search_flags)
    self.search.SetFocus()