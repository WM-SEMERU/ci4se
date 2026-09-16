def validate_format(self, allowed_formats):
    if self.format in allowed_formats:
        return
    ui.error("Export type '{0}' does not accept '{1}' format, only: {2}".
        format(self.type, self.format, allowed_formats))
    sys.exit(1)