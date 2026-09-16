def return_single_convert_numpy(self, object_id, converter, add_args=None):
    return return_single_convert_numpy_base(self.dbpath, self.path_to_set,
        self._set_object, object_id, converter, add_args)