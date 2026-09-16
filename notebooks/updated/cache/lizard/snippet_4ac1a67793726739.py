def printAllWidgets(qApplication, ofType=None):
    print("Application's widgets {}".format('of type: ' + str(ofType) if
        ofType else ''))
    for widget in qApplication.allWidgets():
        if ofType is None or isinstance(widget, ofType):
            print('  {!r}'.format(widget))