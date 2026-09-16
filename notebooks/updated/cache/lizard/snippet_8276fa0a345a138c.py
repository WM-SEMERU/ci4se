def diff_asymmetric(self, catalogue, prime_label, tokenizer, output_fh):
    labels = list(self._set_labels(catalogue))
    if len(labels) < 2:
        raise MalformedQueryError(constants.INSUFFICIENT_LABELS_QUERY_ERROR)
    try:
        labels.remove(prime_label)
    except ValueError:
        raise MalformedQueryError(constants.LABEL_NOT_IN_CATALOGUE_ERROR)
    label_placeholders = self._get_placeholders(labels)
    query = constants.SELECT_DIFF_ASYMMETRIC_SQL.format(label_placeholders)
    parameters = [prime_label, prime_label] + labels
    self._logger.info('Running asymmetric diff query')
    self._logger.debug('Query: {}\nLabels: {}\nPrime label: {}'.format(
        query, labels, prime_label))
    self._log_query_plan(query, parameters)
    cursor = self._conn.execute(query, parameters)
    return self._diff(cursor, tokenizer, output_fh)