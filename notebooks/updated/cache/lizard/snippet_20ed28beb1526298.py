def _drop_no_label_results(self, results, fh):
    results.seek(0)
    results = Results(results, self._tokenizer)
    results.remove_label(self._no_label)
    results.csv(fh)