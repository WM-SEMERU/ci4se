def AskFileForSave(message=None, savedFileName=None, version=None,
    defaultLocation=None, dialogOptionFlags=None, location=None, clientName
    =None, windowTitle=None, actionButtonLabel=None, cancelButtonLabel=None,
    preferenceKey=None, popupExtension=None, eventProc=None, fileType=None,
    fileCreator=None, wanted=None, multiple=None):
    return psidialogs.ask_file(message=message, save=True)