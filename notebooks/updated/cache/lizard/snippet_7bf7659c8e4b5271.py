def remove(self):
    lib.gp_camera_file_delete(self._cam._cam, self.directory.path.encode(),
        self.name.encode(), self._cam._ctx)