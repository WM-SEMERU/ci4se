def _handle_tag_module_refresh(self, tag, data):
    self.module_refresh(force_refresh=data.get('force_refresh', False),
        notify=data.get('notify', False))