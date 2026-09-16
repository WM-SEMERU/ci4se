def persistent_id(self, obj):
    obj_class = None if not hasattr(obj, '__class__') else obj.__class__
    if obj_class is None:
        return None
    if _is_not_pickle_safe_gl_class(obj_class):
        if id(obj) in self.gl_object_memo:
            return None, None, id(obj)
        else:
            relative_filename = str(_uuid.uuid4())
            filename = _os.path.join(self.gl_temp_storage_path,
                relative_filename)
            self.mark_for_delete -= set([filename])
            obj.save(filename)
            self.gl_object_memo.add(id(obj))
            return _get_gl_class_type(obj.__class__), relative_filename, id(obj
                )
    else:
        return None