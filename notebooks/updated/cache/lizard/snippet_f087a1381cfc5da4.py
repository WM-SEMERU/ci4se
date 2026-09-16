def stratSRS2(f, G, y0, tspan, Jmethod=Jkpw, dW=None, J=None):
    return _Roessler2010_SRK2(f, G, y0, tspan, Jmethod, dW, J)