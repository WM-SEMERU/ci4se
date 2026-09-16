def _auto_scroll(self, *args):
    adj = self['scrollable'].get_vadjustment()
    adj.set_value(adj.get_upper() - adj.get_page_size())