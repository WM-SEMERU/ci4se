def OpenSourcePath(self, source_path):
    source_path_spec = path_spec_factory.Factory.NewPathSpec(definitions.
        TYPE_INDICATOR_OS, location=source_path)
    self.AddScanNode(source_path_spec, None)