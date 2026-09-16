def delete_post(self, post_id):
    status = False
    success = 0
    post_id = _as_int(post_id)
    with self._engine.begin() as conn:
        try:
            post_del_statement = self._post_table.delete().where(self.
                _post_table.c.id == post_id)
            conn.execute(post_del_statement)
            success += 1
        except Exception as e:
            self._logger.exception(str(e))
        try:
            user_posts_del_statement = self._user_posts_table.delete().where(
                self._user_posts_table.c.post_id == post_id)
            conn.execute(user_posts_del_statement)
            success += 1
        except Exception as e:
            self._logger.exception(str(e))
        try:
            tag_posts_del_statement = self._tag_posts_table.delete().where(
                self._tag_posts_table.c.post_id == post_id)
            conn.execute(tag_posts_del_statement)
            success += 1
        except Exception as e:
            self._logger.exception(str(e))
    status = success == 3
    return status