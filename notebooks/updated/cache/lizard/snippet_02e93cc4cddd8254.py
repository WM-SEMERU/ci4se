def getPinProperties(cardConnection, featureList=None, controlCode=None):
    if controlCode is None:
        if featureList is None:
            featureList = getFeatureRequest(cardConnection)
        controlCode = hasFeature(featureList, FEATURE_IFD_PIN_PROPERTIES)
    if controlCode is None:
        return {'raw': []}
    response = cardConnection.control(controlCode, [])
    d = {'raw': response, 'LcdLayoutX': response[0], 'LcdLayoutY': response
        [1], 'EntryValidationCondition': response[2], 'TimeOut2': response[3]}
    return d