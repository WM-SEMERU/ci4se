def to_json(self, minimal=True):
    if minimal:
        return json.dumps(self.json_repr(minimal=True), cls=
            MarathonMinimalJsonEncoder, sort_keys=True)
    else:
        return json.dumps(self.json_repr(), cls=MarathonJsonEncoder,
            sort_keys=True)