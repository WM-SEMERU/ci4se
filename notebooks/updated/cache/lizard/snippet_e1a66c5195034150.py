def cleanup(self):
    for key in self._find_keys(identity='image'):
        image_file = self._get(key)
        if image_file and not image_file.exists():
            self.delete(image_file)
    for key in self._find_keys(identity='thumbnails'):
        image_file = self._get(key)
        if image_file:
            thumbnail_keys = self._get(key, identity='thumbnails') or []
            thumbnail_keys_set = set(thumbnail_keys)
            for thumbnail_key in thumbnail_keys:
                if not self._get(thumbnail_key):
                    thumbnail_keys_set.remove(thumbnail_key)
            thumbnail_keys = list(thumbnail_keys_set)
            if thumbnail_keys:
                self._set(key, thumbnail_keys, identity='thumbnails')
                continue
        self._delete(key, identity='thumbnails')