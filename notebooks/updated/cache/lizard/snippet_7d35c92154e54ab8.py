def toPIL(self, **attribs):
    import PIL.Image
    bytes = self.convert('png')
    sfile = io.BytesIO(bytes)
    pil = PIL.Image.open(sfile)
    return pil