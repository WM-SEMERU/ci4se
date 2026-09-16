def Hooper2K(Di, Re, name=None, K1=None, Kinfty=None):
    r
    if name:
        if name in Hooper:
            d = Hooper[name]
            K1, Kinfty = d['K1'], d['Kinfty']
        else:
            raise Exception('Name of fitting not in list')
    elif K1 and Kinfty:
        pass
    else:
        raise Exception('Name of fitting or constants are required')
    return K1 / Re + Kinfty * (1.0 + 1.0 / Di)