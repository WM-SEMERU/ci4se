def on_deleted(self, event):
    if not self._event_error:
        self.logger.info('Change detected from deletion of: %s', event.src_path
            )
        self.compile_dependencies(event.src_path, include_self=False)