def total_bytes_billed(self):
    result = self._job_statistics().get('totalBytesBilled')
    if result is not None:
        result = int(result)
    return result