def set_stencil_func(self, func='always', ref=0, mask=8, face='front_and_back'
    ):
    self.glir.command('FUNC', 'glStencilFuncSeparate', face, func, int(ref),
        int(mask))