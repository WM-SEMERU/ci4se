def _gen_last_current_relation(self, post_id):
    last_post_id = self.get_secure_cookie('last_post_uid')
    if last_post_id:
        last_post_id = last_post_id.decode('utf-8')
    self.set_secure_cookie('last_post_uid', post_id)
    if last_post_id and MPost.get_by_uid(last_post_id):
        self._add_relation(last_post_id, post_id)