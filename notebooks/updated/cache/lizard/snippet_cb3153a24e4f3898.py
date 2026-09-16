def on_draw(self):
    if self.program:
        self.program.draw(self.gl_primitive_type)
    else:
        logger.debug(
            'Skipping drawing visual `%s` because the program has not been built yet.'
            , self)