def project_process(index, start, end):
    results = {'bmi_metrics': [BMI(index, start, end)],
        'time_to_close_metrics': [DaysToCloseAverage(index, start, end),
        DaysToCloseMedian(index, start, end)],
        'time_to_close_review_metrics': [], 'patchsets_metrics': []}
    return results