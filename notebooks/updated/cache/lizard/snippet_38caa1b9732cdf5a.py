def xgroup_setid(self, stream, group_name, latest_id='$'):
    fut = self.execute(b'XGROUP', b'SETID', stream, group_name, latest_id)
    return wait_ok(fut)