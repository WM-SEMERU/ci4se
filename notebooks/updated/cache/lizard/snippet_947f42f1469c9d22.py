def add_permissions_menu(self, view_menu_name):
    self.add_view_menu(view_menu_name)
    pv = self.find_permission_view_menu('menu_access', view_menu_name)
    if not pv:
        pv = self.add_permission_view_menu('menu_access', view_menu_name)
        role_admin = self.find_role(self.auth_role_admin)
        self.add_permission_role(role_admin, pv)