def add_positional_features(tensor: torch.Tensor, min_timescale: float=1.0,
    max_timescale: float=10000.0):
    _, timesteps, hidden_dim = tensor.size()
    timestep_range = get_range_vector(timesteps, get_device_of(tensor)
        ).data.float()
    num_timescales = hidden_dim // 2
    timescale_range = get_range_vector(num_timescales, get_device_of(tensor)
        ).data.float()
    log_timescale_increments = math.log(float(max_timescale) / float(
        min_timescale)) / float(num_timescales - 1)
    inverse_timescales = min_timescale * torch.exp(timescale_range * -
        log_timescale_increments)
    scaled_time = timestep_range.unsqueeze(1) * inverse_timescales.unsqueeze(0)
    sinusoids = torch.cat([torch.sin(scaled_time), torch.cos(scaled_time)], 1)
    if hidden_dim % 2 != 0:
        sinusoids = torch.cat([sinusoids, sinusoids.new_zeros(timesteps, 1)], 1
            )
    return tensor + sinusoids.unsqueeze(0)