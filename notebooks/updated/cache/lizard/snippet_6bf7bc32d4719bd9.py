def is_class_or_module(self):
    if isinstance(self.obj, ObjectDouble):
        return self.obj.is_class
    return isclass(self.doubled_obj) or ismodule(self.doubled_obj)