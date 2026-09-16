def predict(self, recording, result_format=None):
    evaluate = utils.evaluate_model_single_recording_preloaded
    results = evaluate(self.preprocessing_queue, self.feature_list, self.
        model, self.output_semantics, recording)
    if result_format == 'LaTeX':
        for i in range(len(results)):
            results[i]['semantics'] = results[i]['semantics'].split(';')[1]
    for i in range(len(results)):
        splitted = results[i]['semantics'].split(';')
        results[i]['complete_latex'] = splitted[1]
    return results