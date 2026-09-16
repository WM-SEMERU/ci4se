def env_updated(self, kb_app, sphinx_app: Sphinx, sphinx_env:
    BuildEnvironment, resource):
    docname = resource.docname
    srcdir = sphinx_app.env.srcdir
    source_imgpath = self.source_filename(docname, srcdir)
    build_dir = sphinx_app.outdir
    docpath = Path(docname)
    parent = docpath.parent
    target_imgpath = str(Path(build_dir, parent, self.filename))
    target_dir = Path(build_dir, parent)
    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_imgpath, target_imgpath)