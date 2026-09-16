def wait(self, timeout=None):
    poll = 30
    while not self._is_complete:
        try:
            query_result = self._api.jobs_query_results(self._job_id,
                project_id=self._context.project_id, page_size=0, timeout=
                poll * 1000)
        except Exception as e:
            raise e
        if query_result['jobComplete']:
            if 'totalBytesProcessed' in query_result:
                self._bytes_processed = int(query_result['totalBytesProcessed']
                    )
            self._cache_hit = query_result.get('cacheHit', None)
            if 'totalRows' in query_result:
                self._total_rows = int(query_result['totalRows'])
            break
        if timeout is not None:
            timeout -= poll
            if timeout <= 0:
                break
    self._refresh_state()
    return self