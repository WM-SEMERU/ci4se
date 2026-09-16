def get_tab(self, tab_name, allow_disabled=False):
    tab = self._tabs.get(tab_name, None)
    if tab and tab._allowed and (tab._enabled or allow_disabled):
        return tab
    return None