def system_generate_batch_inputs(input_params={}, always_retry=True, **kwargs):
    return DXHTTPRequest('/system/generateBatchInputs', input_params,
        always_retry=always_retry, **kwargs)