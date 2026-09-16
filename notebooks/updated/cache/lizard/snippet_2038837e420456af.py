def trace_memory_stop(self):
    self.trace_memory_clean_caches()
    objgraph.show_growth(limit=30)
    trace_type = context.get_current_config()['trace_memory_type']
    if trace_type:
        filename = '%s/%s-%s.png' % (context.get_current_config()[
            'trace_memory_output_dir'], trace_type, self.id)
        chain = objgraph.find_backref_chain(random.choice(objgraph.by_type(
            trace_type)), objgraph.is_proper_module)
        objgraph.show_chain(chain, filename=filename)
        del filename
        del chain
    gc.collect()
    self._memory_stop = self.worker.get_memory()['total']
    diff = self._memory_stop - self._memory_start
    context.log.debug('Memory diff for job %s : %s' % (self.id, diff))
    self.collection.update({'_id': self.id}, {'$set': {'memory_diff': diff}
        }, w=1)