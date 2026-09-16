def sendRemoteImage(self, image_url, message=None, thread_id=None,
    thread_type=ThreadType.USER):
    return self.sendRemoteFiles(file_urls=[image_url], message=message,
        thread_id=thread_id, thread_type=thread_type)