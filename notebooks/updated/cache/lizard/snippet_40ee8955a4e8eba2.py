def expose_init(self, *args):
    gldrawable = self.get_gl_drawable()
    glcontext = self.get_gl_context()
    if not gldrawable or not gldrawable.gl_begin(glcontext):
        return False
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glInitNames()
    glPushName(0)
    self.name_counter = 1
    return False