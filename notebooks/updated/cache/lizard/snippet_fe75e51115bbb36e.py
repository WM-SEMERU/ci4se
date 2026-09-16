def modifierFactor(chart, factor, factorObj, otherObj, aspList):
    asp = aspects.aspectType(factorObj, otherObj, aspList)
    if asp != const.NO_ASPECT:
        return {'factor': factor, 'aspect': asp, 'objID': otherObj.id,
            'element': otherObj.element()}
    return None