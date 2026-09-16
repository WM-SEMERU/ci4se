def GetRootFileEntry(self):
    path_spec = vshadow_path_spec.VShadowPathSpec(location=self.
        LOCATION_ROOT, parent=self._path_spec.parent)
    return self.GetFileEntryByPathSpec(path_spec)