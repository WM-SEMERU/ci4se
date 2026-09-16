def to_legacy_urlsafe(self, location_prefix=None):
    if location_prefix is None:
        project_id = self.project
    else:
        project_id = location_prefix + self.project
    reference = _app_engine_key_pb2.Reference(app=project_id, path=
        _to_legacy_path(self._path), name_space=self.namespace)
    raw_bytes = reference.SerializeToString()
    return base64.urlsafe_b64encode(raw_bytes).strip(b'=')