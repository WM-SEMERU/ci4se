def add_permissions_view(self, base_permissions, view_menu):
    view_menu_db = self.add_view_menu(view_menu)
    perm_views = self.find_permissions_view_menu(view_menu_db)
    if not perm_views:
        for permission in base_permissions:
            pv = self.add_permission_view_menu(permission, view_menu)
            role_admin = self.find_role(self.auth_role_admin)
            self.add_permission_role(role_admin, pv)
    else:
        role_admin = self.find_role(self.auth_role_admin)
        for permission in base_permissions:
            if not self.exist_permission_on_views(perm_views, permission):
                pv = self.add_permission_view_menu(permission, view_menu)
                self.add_permission_role(role_admin, pv)
        for perm_view in perm_views:
            if perm_view.permission.name not in base_permissions:
                roles = self.get_all_roles()
                perm = self.find_permission(perm_view.permission.name)
                for role in roles:
                    self.del_permission_role(role, perm)
                self.del_permission_view_menu(perm_view.permission.name,
                    view_menu)
            elif perm_view not in role_admin.permissions:
                self.add_permission_role(role_admin, perm_view)