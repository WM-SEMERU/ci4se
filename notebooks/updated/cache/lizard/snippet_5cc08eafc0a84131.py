def launch_from_template(self, template_path, notebook_dir=None, overwrite=
    False, output_name=None, create_dir=False, no_browser=False, **kwargs):
    template_path = template_path.abspath()
    if output_name is None:
        output_name = template_path.name
    if notebook_dir is None:
        notebook_dir = path(os.getcwd())
    else:
        notebook_dir = path(notebook_dir).abspath()
    if template_path.parent.realpath() == notebook_dir.realpath():
        raise IOError(
            'Notebook directory must not be the parent directory of the template file.'
            )
    else:
        output_path = notebook_dir.joinpath(output_name)
        if output_path.isfile() and not overwrite:
            raise IOError('Notebook already exists with same name.')
        if create_dir:
            notebook_dir.mkdirs_p()
        template_path.copy(output_path)
        notebook_path = output_path
    session = self.get_session(notebook_dir=notebook_dir, **kwargs)
    if not no_browser:
        session.open(notebook_path.name)