def _extract_links_from_asset_tags_in_text(self, text):
    asset_tags_map = self._extract_asset_tags(text)
    ids = list(iterkeys(asset_tags_map))
    if not ids:
        return {}
    asset_urls = self._extract_asset_urls(ids)
    supplement_links = {}
    for asset in asset_urls:
        title = clean_filename(asset_tags_map[asset['id']]['name'], self.
            _unrestricted_filenames)
        extension = clean_filename(asset_tags_map[asset['id']]['extension']
            .strip(), self._unrestricted_filenames)
        url = asset['url'].strip()
        if extension not in supplement_links:
            supplement_links[extension] = []
        supplement_links[extension].append((url, title))
    return supplement_links