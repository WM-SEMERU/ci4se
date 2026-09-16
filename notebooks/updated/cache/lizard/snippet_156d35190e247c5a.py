def value_loss(value_net_apply, value_net_params, observations, rewards,
    reward_mask, gamma=0.99):
    B, T = rewards.shape
    assert (B, T + 1) == observations.shape[:2]
    value_prediction = value_net_apply(observations, value_net_params)
    assert (B, T + 1, 1) == value_prediction.shape
    return value_loss_given_predictions(value_prediction, rewards,
        reward_mask, gamma)