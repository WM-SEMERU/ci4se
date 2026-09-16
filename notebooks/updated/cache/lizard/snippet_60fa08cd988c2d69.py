def acceleration_of_satellite(position, mass):
    F_x, F_y = force_on_satellite(position, mass)
    return F_x / mass, F_y / mass