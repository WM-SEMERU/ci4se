def draw(self, mode='triangles'):
    gl.glDepthMask(0)
    Collection.draw(self, mode)
    gl.glDepthMask(1)