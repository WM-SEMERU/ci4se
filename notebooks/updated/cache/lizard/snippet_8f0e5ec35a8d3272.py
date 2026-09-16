def read_iou_stdout(self):
    output = ''
    if self._iou_stdout_file:
        try:
            with open(self._iou_stdout_file, 'rb') as file:
                output = file.read().decode('utf-8', errors='replace')
        except OSError as e:
            log.warn('could not read {}: {}'.format(self._iou_stdout_file, e))
    return output