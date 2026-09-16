def copy(self):
    uv = self.uv
    if uv is not None:
        uv = uv.copy()
    copied = TextureVisuals(uv=uv, material=copy.deepcopy(self.material))
    return copied