def _fetch_dataframe(self):

    def reshape(training_summary):
        out = {}
        for k, v in training_summary['TunedHyperParameters'].items():
            try:
                v = float(v)
            except (TypeError, ValueError):
                pass
            out[k] = v
        out['TrainingJobName'] = training_summary['TrainingJobName']
        out['TrainingJobStatus'] = training_summary['TrainingJobStatus']
        out['FinalObjectiveValue'] = training_summary.get(
            'FinalHyperParameterTuningJobObjectiveMetric', {}).get('Value')
        start_time = training_summary.get('TrainingStartTime', None)
        end_time = training_summary.get('TrainingEndTime', None)
        out['TrainingStartTime'] = start_time
        out['TrainingEndTime'] = end_time
        if start_time and end_time:
            out['TrainingElapsedTimeSeconds'] = (end_time - start_time
                ).total_seconds()
        return out
    df = pd.DataFrame([reshape(tjs) for tjs in self.training_job_summaries()])
    return df