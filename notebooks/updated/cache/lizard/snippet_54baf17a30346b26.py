def cast(cls, c):
    if isinstance(c, Complete):
        return c
    elif isinstance(c, Translation):
        return Complete(np.identity(3, float), c.t)
    elif isinstance(c, Rotation):
        return Complete(c.r, np.zeros(3, float))