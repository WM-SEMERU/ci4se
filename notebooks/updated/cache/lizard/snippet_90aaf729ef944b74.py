def _updateable(self, obj):
    if obj.latest_version is None or obj.is_editable:
        return None
    else:
        return obj.latest_version != obj.current_version