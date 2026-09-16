def unbind(self, binding):
    username = self.backend.config.generate_binding_username(binding)
    try:
        self.backend.atlas.DatabaseUsers.delete_a_database_user(username)
    except ErrAtlasNotFound:
        pass
    self.backend.storage.remove(binding)