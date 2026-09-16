def _parse_mtllibs(self):
    for mtllib in self.meta.mtllibs:
        try:
            materials = self.material_parser_cls(os.path.join(self.path,
                mtllib), encoding=self.encoding, strict=self.strict).materials
        except IOError:
            raise IOError('Failed to load mtl file:'.format(os.path.join(
                self.path, mtllib)))
        for name, material in materials.items():
            self.wavefront.materials[name] = material