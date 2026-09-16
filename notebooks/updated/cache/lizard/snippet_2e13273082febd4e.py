def _genTex2D(self):
    for face in range(6):
        gl.glTexImage2D(self.target0 + face, 0, self.internal_fmt, self.
            width, self.height, 0, self.pixel_fmt, gl.GL_UNSIGNED_BYTE, 0)