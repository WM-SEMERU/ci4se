def delete_menu(self, menu):
    if menu.parent is None:
        del self.menus[menu.name()]
    menu._delete()