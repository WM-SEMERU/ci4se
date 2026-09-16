def itoSRI2(f, G, y0, tspan, Imethod=Ikpw, dW=None, I=None):
    return _Roessler2010_SRK2(f, G, y0, tspan, Imethod, dW, I)