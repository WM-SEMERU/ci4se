def mark_as_duplicate(self, duplicated_cid, master_cid, msg=''):
    content_id_from = self.get_post(duplicated_cid)['id']
    content_id_to = self.get_post(master_cid)['id']
    params = {'cid_dupe': content_id_from, 'cid_to': content_id_to, 'msg': msg}
    return self._rpc.content_mark_duplicate(params)