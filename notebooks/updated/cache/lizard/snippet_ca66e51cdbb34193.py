def dump(self, blob, stream):
    json.dump(blob, stream, indent=self.indent, sort_keys=True, separators=
        self.separators)