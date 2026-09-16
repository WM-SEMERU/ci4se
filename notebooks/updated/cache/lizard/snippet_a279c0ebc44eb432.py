def clean():
    d = ['build', 'dist', 'scikits.audiolab.egg-info', HTML_DESTDIR,
        PDF_DESTDIR]
    for i in d:
        paver.path.path(i).rmtree()
    (paver.path.path('docs') / options.sphinx.builddir).rmtree()