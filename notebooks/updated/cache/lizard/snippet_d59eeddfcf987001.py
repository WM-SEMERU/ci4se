def _GetPurgeMessage(most_recent_step, most_recent_wall_time, event_step,
    event_wall_time, num_expired):
    return (
        'Detected out of order event.step likely caused by a TensorFlow restart. Purging {} expired tensor events from Tensorboard display between the previous step: {} (timestamp: {}) and current step: {} (timestamp: {}).'
        .format(num_expired, most_recent_step, most_recent_wall_time,
        event_step, event_wall_time))