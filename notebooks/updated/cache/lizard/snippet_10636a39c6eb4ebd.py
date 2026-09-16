def get_html_labels_weights(self, data):
    all_html = []
    all_labels = []
    all_weights = []
    for html, content, comments in data:
        all_html.append(html)
        labels, weights = self._get_labels_and_weights(content, comments)
        all_labels.append(labels)
        all_weights.append(weights)
    return np.array(all_html), np.array(all_labels), np.array(all_weights)