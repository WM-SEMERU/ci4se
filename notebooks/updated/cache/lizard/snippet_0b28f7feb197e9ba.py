def load_constants():
    G: float = 6.67408e-11
    body_name = ['sun', 'moon', 'mercury', 'venus', 'earth', 'mars',
        'jupiter', 'saturn', 'uranus', 'neptune']
    mass_earth: float = 5.9722e+24
    mass: Dict[str, float] = {'sun': mass_earth * 332946.0487, 'moon': 
        mass_earth * 0.012300037, 'mercury': mass_earth * 0.0553, 'venus': 
        mass_earth * 0.815, 'earth': mass_earth * 1.0, 'mars': mass_earth *
        0.107, 'jupiter': mass_earth * 317.8, 'saturn': mass_earth * 95.2,
        'uranus': mass_earth * 14.5, 'neptune': mass_earth * 17.1}
    radius: Dict[str, float] = {'sun': 695000000.0, 'moon': 1738000.0,
        'mercury': 2440000.0, 'venus': 6052000.0, 'earth': 6378000.0,
        'mars': 3397000.0, 'jupiter': 71492000.0, 'saturn': 60268000.0,
        'uranus': 35559000.0, 'neptune': 24766000.0}
    return G, body_name, mass, radius