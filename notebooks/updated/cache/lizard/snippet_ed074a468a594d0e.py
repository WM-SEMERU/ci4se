async def async_enqueue_download(self, resource):
    worker = self.pick_sticky(resource.url_string)
    await worker.enqueue(enums.Task.DOWNLOAD, (resource,))