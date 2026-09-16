def predict(self, parsed_json):
    evaluate = utils.evaluate_model_single_recording_preloaded
    results = evaluate(self.preprocessing_queue, self.feature_list, self.
        model, self.output_semantics, json.dumps(parsed_json['data']),
        parsed_json['id'])
    return results