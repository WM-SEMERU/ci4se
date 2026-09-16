def search_on_web(self, *args):
    current_term = self.get_notebook().get_current_terminal()
    if current_term.get_has_selection():
        current_term.copy_clipboard()
        guake_clipboard = Gtk.Clipboard.get_default(self.window.get_display())
        search_query = guake_clipboard.wait_for_text()
        search_query = quote_plus(search_query)
        if search_query:
            search_url = 'https://www.google.com/#q={!s}&safe=off'.format(
                search_query)
            Gtk.show_uri(self.window.get_screen(), search_url,
                get_server_time(self.window))
    return True