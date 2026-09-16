def Nu_vertical_cylinder_Griffiths_Davis_Morgan(Pr, Gr, turbulent=None):
    r
    Ra = Pr * Gr
    if turbulent or Ra > 1000000000.0 and turbulent is None:
        Nu = 0.0782 * Ra ** 0.357
    else:
        Nu = 0.67 * Ra ** 0.25
    return Nu