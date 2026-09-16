async def get(self, target_format, target_size, size_tolerance_prct,
    out_filepath):
    if self.source_quality.value <= CoverSourceQuality.LOW.value:
        logging.getLogger('Cover').warning(
            'Cover is from a potentially unreliable source and may be unrelated to the search'
            )
    images_data = []
    for i, url in enumerate(self.urls):
        logging.getLogger('Cover').info(
            "Downloading cover '%s' (part %u/%u)..." % (url, i + 1, len(
            self.urls)))
        headers = {}
        self.source.updateHttpHeaders(headers)

        async def pre_cache_callback(img_data):
            return await __class__.crunch(img_data, self.format)
        store_in_cache_callback, image_data = await self.source.http.query(url,
            headers=headers, verify=False, cache=__class__.image_cache,
            pre_cache_callback=pre_cache_callback)
        await store_in_cache_callback()
        images_data.append(image_data)
    need_format_change = self.format != target_format
    need_size_change = max(self.size) > target_size and abs(max(self.size) -
        target_size) > target_size * size_tolerance_prct / 100
    need_join = len(images_data) > 1
    if need_join or need_format_change or need_size_change:
        image_data = self.postProcess(images_data, target_format if
            need_format_change else None, target_size if need_size_change else
            None)
        image_data = await __class__.crunch(image_data, target_format)
    with open(out_filepath, 'wb') as file:
        file.write(image_data)