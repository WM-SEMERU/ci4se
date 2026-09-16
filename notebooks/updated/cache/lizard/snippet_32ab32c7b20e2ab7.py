def get_open_filenames(self):
    editorstack = self.editorstacks[0]
    filenames = []
    filenames += [finfo.filename for finfo in editorstack.data]
    return filenames