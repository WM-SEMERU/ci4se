def run(self):
    while not self._abort:
        hashes = self._GetHashes(self._hash_queue, self.hashes_per_batch)
        if hashes:
            time_before_analysis = time.time()
            hash_analyses = self.Analyze(hashes)
            current_time = time.time()
            self.seconds_spent_analyzing += current_time - time_before_analysis
            self.analyses_performed += 1
            for hash_analysis in hash_analyses:
                self._hash_analysis_queue.put(hash_analysis)
                self._hash_queue.task_done()
            time.sleep(self.wait_after_analysis)
        else:
            time.sleep(self.EMPTY_QUEUE_WAIT_TIME)