def override_role_permissions(self):
    data = request.get_json(force=True)
    role_name = data['role_name']
    databases = data['database']
    db_ds_names = set()
    for dbs in databases:
        for schema in dbs['schema']:
            for ds_name in schema['datasources']:
                fullname = utils.get_datasource_full_name(dbs['name'],
                    ds_name, schema=schema['name'])
                db_ds_names.add(fullname)
    existing_datasources = ConnectorRegistry.get_all_datasources(db.session)
    datasources = [d for d in existing_datasources if d.full_name in
        db_ds_names]
    role = security_manager.find_role(role_name)
    role.permissions = []
    granted_perms = []
    for datasource in datasources:
        view_menu_perm = security_manager.find_permission_view_menu(
            view_menu_name=datasource.perm, permission_name='datasource_access'
            )
        if view_menu_perm and view_menu_perm.view_menu:
            role.permissions.append(view_menu_perm)
            granted_perms.append(view_menu_perm.view_menu.name)
    db.session.commit()
    return self.json_response({'granted': granted_perms, 'requested': list(
        db_ds_names)}, status=201)