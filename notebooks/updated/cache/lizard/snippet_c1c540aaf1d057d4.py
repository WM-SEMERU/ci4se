def classinstances(cls):
    l = [i for i in cls.allinstances() if type(i) == cls]
    return l