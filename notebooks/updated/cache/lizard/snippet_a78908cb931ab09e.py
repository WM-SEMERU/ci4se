def has_roles(self, *requirements):
    user_manager = current_app.user_manager
    role_names = user_manager.db_manager.get_user_roles(self)
    for requirement in requirements:
        if isinstance(requirement, (list, tuple)):
            tuple_of_role_names = requirement
            authorized = False
            for role_name in tuple_of_role_names:
                if role_name in role_names:
                    authorized = True
                    break
            if not authorized:
                return False
        else:
            role_name = requirement
            if not role_name in role_names:
                return False
    return True