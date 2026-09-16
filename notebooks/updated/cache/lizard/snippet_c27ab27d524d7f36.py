def qmax_boiling(rhol=None, rhog=None, sigma=None, Hvap=None, D=None, P=
    None, Pc=None, Method=None, AvailableMethods=False):
    r

    def list_methods():
        methods = []
        if all((sigma, Hvap, rhol, rhog, D)):
            methods.append('Serth-HEDH')
        if all((sigma, Hvap, rhol, rhog)):
            methods.append('Zuber')
        if all((P, Pc)):
            methods.append('HEDH-Montinsky')
        return methods
    if AvailableMethods:
        return list_methods()
    if not Method:
        methods = list_methods()
        if methods == []:
            raise Exception(
                'Insufficient property or geometry data for any method.')
        Method = methods[0]
    if Method == 'Serth-HEDH':
        return Serth_HEDH(D=D, sigma=sigma, Hvap=Hvap, rhol=rhol, rhog=rhog)
    elif Method == 'Zuber':
        return Zuber(sigma=sigma, Hvap=Hvap, rhol=rhol, rhog=rhog)
    elif Method == 'HEDH-Montinsky':
        return HEDH_Montinsky(P=P, Pc=Pc)
    else:
        raise Exception(
            "Correlation name not recognized; options are 'Serth-HEDH', 'Zuber' and 'HEDH-Montinsky'"
            )