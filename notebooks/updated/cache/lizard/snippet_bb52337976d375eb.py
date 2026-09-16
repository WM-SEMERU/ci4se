def outputs(self):
    outputs = self._outputs()
    if len(outputs) != len(self._output_layer_expected):
        raise Exception(
            'The computed count of output layers is wrong. It should be {expected} but the count is {count}.'
            .format(expected=len(self._output_layer_expected), count=len(
            outputs)))
    return outputs