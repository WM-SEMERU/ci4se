def get_ticks(self):
    tick_distance = []
    tick_labels = []
    previous_label = self._bs.qpoints[0].label
    previous_branch = self._bs.branches[0]['name']
    for i, c in enumerate(self._bs.qpoints):
        if c.label is not None:
            tick_distance.append(self._bs.distance[i])
            this_branch = None
            for b in self._bs.branches:
                if b['start_index'] <= i <= b['end_index']:
                    this_branch = b['name']
                    break
            if c.label != previous_label and previous_branch != this_branch:
                label1 = c.label
                if label1.startswith('\\') or label1.find('_') != -1:
                    label1 = '$' + label1 + '$'
                label0 = previous_label
                if label0.startswith('\\') or label0.find('_') != -1:
                    label0 = '$' + label0 + '$'
                tick_labels.pop()
                tick_distance.pop()
                tick_labels.append(label0 + '$\\mid$' + label1)
            elif c.label.startswith('\\') or c.label.find('_') != -1:
                tick_labels.append('$' + c.label + '$')
            else:
                tick_labels.append(c.label)
            previous_label = c.label
            previous_branch = this_branch
    return {'distance': tick_distance, 'label': tick_labels}