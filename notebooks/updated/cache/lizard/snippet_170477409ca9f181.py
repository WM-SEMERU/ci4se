def set_weights(params, new_params):
    for param, new_param in zip(params, new_params):
        param.data.copy_(new_param.data)