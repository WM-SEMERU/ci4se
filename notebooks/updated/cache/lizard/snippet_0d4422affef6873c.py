def put_summary(self, summary):
    if isinstance(summary, six.binary_type):
        summary = tf.Summary.FromString(summary)
    assert isinstance(summary, tf.Summary), type(summary)
    for val in summary.value:
        if val.WhichOneof('value') == 'simple_value':
            val.tag = re.sub('tower[0-9]+/', '', val.tag)
            suffix = '-summary'
            if val.tag.endswith(suffix):
                val.tag = val.tag[:-len(suffix)]
            self._dispatch(lambda m: m.process_scalar(val.tag, val.
                simple_value))
    self._dispatch(lambda m: m.process_summary(summary))