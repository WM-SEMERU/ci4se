def bundle(self, app, results_dir):
    assert isinstance(app, BundleCreate.App)
    bundle_dir = self.get_bundle_dir(app.id, results_dir)
    self.context.log.debug('creating {}'.format(os.path.relpath(bundle_dir,
        get_buildroot())))
    safe_mkdir(bundle_dir, clean=True)
    classpath = OrderedSet()
    lib_dir = os.path.join(bundle_dir, self.LIBS_DIR)
    if not app.deployjar:
        os.mkdir(lib_dir)
        consolidated_classpath = self.context.products.get_data(
            'consolidated_classpath')
        classpath.update(ClasspathProducts.create_canonical_classpath(
            consolidated_classpath, app.target.closure(bfs=True, **self.
            _target_closure_kwargs), lib_dir, internal_classpath_only=False,
            excludes=app.binary.deploy_excludes))
    bundle_jar = os.path.join(bundle_dir, '{}.jar'.format(app.binary.basename))
    with self.monolithic_jar(app.binary, bundle_jar, manifest_classpath=
        classpath) as jar:
        self.add_main_manifest_entry(jar, app.binary)
        classpath.update([jar.path])
    if app.binary.shading_rules:
        for jar_path in classpath:
            self.shade_jar(shading_rules=app.binary.shading_rules, jar_path
                =jar_path)
    self.symlink_bundles(app, bundle_dir)
    return bundle_dir