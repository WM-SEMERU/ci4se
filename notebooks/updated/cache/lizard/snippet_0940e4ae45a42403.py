def get_tab_text(self, index, is_modified=None, is_readonly=None):
    files_path_list = [finfo.filename for finfo in self.data]
    fname = self.data[index].filename
    fname = sourcecode.disambiguate_fname(files_path_list, fname)
    return self.__modified_readonly_title(fname, is_modified, is_readonly)