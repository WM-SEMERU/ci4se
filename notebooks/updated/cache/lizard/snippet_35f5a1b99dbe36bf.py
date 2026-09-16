def Darby3K(NPS=None, Re=None, name=None, K1=None, Ki=None, Kd=None):
    r
    if name:
        if name in Darby:
            d = Darby[name]
            K1, Ki, Kd = d['K1'], d['Ki'], d['Kd']
        else:
            raise Exception('Name of fitting not in list')
    elif K1 and Ki and Kd:
        pass
    else:
        raise Exception('Name of fitting or constants are required')
    return K1 / Re + Ki * (1.0 + Kd / NPS ** 0.3)