def get_cached_item(self, path):
    item_path = '%s/%s/%s' % (current_app.static_folder, self.cache_folder,
        path.strip('/'))
    if os.path.isfile(item_path):
        try:
            return Image.open(item_path)
        except IOError as err:
            LOGGER.warning(
                'Cached file not found on path "%s" with error: %s' % (
                item_path, str(err)))
            return False
    else:
        return False