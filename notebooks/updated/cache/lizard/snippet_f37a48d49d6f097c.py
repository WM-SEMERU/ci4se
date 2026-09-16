def set_renderer(self, renderer):
    viewport = None
    if renderer == 'opengl':
        from enaml.qt.QtWidgets import QOpenGLWidget
        viewport = QOpenGLWidget()
    elif renderer == 'default':
        try:
            from enaml.qt.QtWidgets import QOpenGLWidget
            viewport = QOpenGLWidget()
        except ImportError as e:
            warnings.warn('QOpenGLWidget could not be imported: {}'.format(e))
    self.widget.setViewport(viewport)