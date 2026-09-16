def delete(self, key, *keys):
    fut = self.execute(b'DEL', key, *keys)
    return wait_convert(fut, int)