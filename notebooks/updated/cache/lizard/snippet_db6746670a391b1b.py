def init_app(self, app, **kwargs):
    self.init_db(app, **kwargs)
    app.config.setdefault('ALEMBIC', {'script_location': pkg_resources.
        resource_filename('invenio_db', 'alembic'), 'version_locations': [(
        base_entry.name, pkg_resources.resource_filename(base_entry.
        module_name, os.path.join(*base_entry.attrs))) for base_entry in
        pkg_resources.iter_entry_points('invenio_db.alembic')]})
    self.alembic.init_app(app)
    app.extensions['invenio-db'] = self
    app.cli.add_command(db_cmd)