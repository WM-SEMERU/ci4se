def onImageChange(self, mid=None, author_id=None, new_image=None, thread_id
    =None, thread_type=ThreadType.GROUP, ts=None, msg=None):
    log.info('{} changed thread image in {}'.format(author_id, thread_id))