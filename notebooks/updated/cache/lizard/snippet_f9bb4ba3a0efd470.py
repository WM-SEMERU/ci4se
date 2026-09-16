def result_report_class_wise_average(self):
    results = self.results_class_wise_average_metrics()
    output = self.ui.section_header(
        'Class-wise average metrics (macro-average)', indent=2) + '\n'
    output += self.ui.line('Accuracy', indent=2) + '\n'
    output += self.ui.data(field='Accuracy', value=float(results['accuracy'
        ]['accuracy']) * 100, unit='%', indent=4) + '\n'
    return output