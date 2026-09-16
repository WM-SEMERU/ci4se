def provide_plugs(self, plug_name_map):
    return {name: self._plugs_by_type[cls] for name, cls in plug_name_map}