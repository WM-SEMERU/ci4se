def cloud_predict(model_name, model_version, data):
    import google.datalab.ml as ml
    if isinstance(data, pd.DataFrame):
        string_buffer = io.StringIO()
        data.to_csv(string_buffer, header=None, index=False)
        input_data = string_buffer.getvalue().split('\n')
        input_data = [line for line in input_data if line]
    else:
        input_data = data
    predictions = ml.ModelVersions(model_name).predict(model_version,
        input_data)
    df = pd.DataFrame(columns=sorted(predictions[0].keys()))
    for i in range(len(predictions)):
        for k, v in predictions[i].iteritems():
            df.loc[i, k] = v
    return df