def setup(app):
    from sphinx.application import Sphinx
    if not isinstance(app, Sphinx):
        return
    app.connect('autodoc-process-docstring', process_docstring)
    return napoleon_setup(app)