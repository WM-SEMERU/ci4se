def overwrite(self, mesh):
    self.DeepCopy(mesh)
    if is_vtki_obj(mesh):
        self.copy_meta_from(mesh)