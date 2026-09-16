def _rename_objects_pretty(self):
    self._global_ns = dict([(kwd, None) for kwd in gloo.util.KEYWORDS])
    self._shader_ns = dict([(shader, {}) for shader in self.shaders])
    obj_shaders = {}
    for shader_name, deps in self._shader_deps.items():
        for dep in deps:
            for name in dep.static_names():
                self._global_ns[name] = None
            obj_shaders.setdefault(dep, []).append(shader_name)
    name_index = {}
    for obj, shaders in obj_shaders.items():
        name = obj.name
        if self._name_available(obj, name, shaders):
            self._assign_name(obj, name, shaders)
        else:
            while True:
                index = name_index.get(name, 0) + 1
                name_index[name] = index
                ext = '_%d' % index
                new_name = name[:32 - len(ext)] + ext
                if self._name_available(obj, new_name, shaders):
                    self._assign_name(obj, new_name, shaders)
                    break