def results_class_wise_metrics(self):
    results = {}
    for event_label in self.event_label_list:
        if event_label not in results:
            results[event_label] = {}
        results[event_label]['f_measure'] = self.class_wise_f_measure(
            event_label)
        results[event_label]['accuracy'] = self.class_wise_accuracy(event_label
            )
        results[event_label]['error_rate'] = self.class_wise_error_rate(
            event_label)
        results[event_label]['count'] = self.class_wise_count(event_label)
    return results