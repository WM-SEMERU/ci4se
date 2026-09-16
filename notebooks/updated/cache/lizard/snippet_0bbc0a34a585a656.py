def _gsa_update_velocity(velocity, acceleration):
    new_velocity = []
    for vel, acc in zip(velocity, acceleration):
        new_velocity.append(random.uniform(0.0, 1.0) * vel + acc)
    return new_velocity