def close(self, file_des):
    file_handle = self.filesystem.get_open_file(file_des)
    file_handle.close()