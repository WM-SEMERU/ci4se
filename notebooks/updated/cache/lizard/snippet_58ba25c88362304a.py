def return_markers(self):
    markers = []
    triggers = self._triggers
    DTYPE_MAX = iinfo(triggers.dtype['sample']).max
    triggers = triggers[triggers['sample'] != DTYPE_MAX]
    for trig in triggers:
        markers.append({'name': str(trig['code']), 'start': trig['sample'] /
            self._s_freq, 'end': trig['sample'] / self._s_freq})
    return markers