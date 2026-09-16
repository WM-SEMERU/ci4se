def geometry_identifiers(self):
    identifiers = {mesh.identifier_md5: name for name, mesh in self.
        geometry.items()}
    return identifiers