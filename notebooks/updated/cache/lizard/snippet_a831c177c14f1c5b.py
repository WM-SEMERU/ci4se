def decompress(self, output_path):
    self.log(["Decompressing the container into '%s'", output_path])
    if not self.exists():
        self.log_exc('This container does not exist. Wrong path?', None,
            True, TypeError)
    if self.actual_container is None:
        self.log_exc('The actual container object has not been set', None,
            True, TypeError)
    if not gf.directory_exists(output_path):
        self.log_exc('The output path is not an existing directory', None,
            True, ValueError)
    if not self.is_safe:
        self.log_exc('This container contains unsafe entries', None, True,
            ValueError)
    self.actual_container.decompress(output_path)