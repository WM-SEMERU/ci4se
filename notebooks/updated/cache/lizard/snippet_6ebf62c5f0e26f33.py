def samefile(self, other_path):
    if hasattr(os.path, 'samestat'):
        st = self.stat()
        try:
            other_st = other_path.stat()
        except AttributeError:
            other_st = os.stat(other_path)
        return os.path.samestat(st, other_st)
    else:
        filename1 = six.text_type(self)
        filename2 = six.text_type(other_path)
        st1 = _win32_get_unique_path_id(filename1)
        st2 = _win32_get_unique_path_id(filename2)
        return st1 == st2