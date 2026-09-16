def setiddname(cls, iddname, testing=False):
    if cls.iddname == None:
        cls.iddname = iddname
        cls.idd_info = None
        cls.block = None
    elif cls.iddname == iddname:
        pass
    elif testing == False:
        errortxt = 'IDD file is set to: %s' % (cls.iddname,)
        raise IDDAlreadySetError(errortxt)