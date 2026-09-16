def is_retaincase(bunchdt, data, commdct, idfobject, fieldname):
    thiscommdct = getfieldcomm(bunchdt, data, commdct, idfobject, fieldname)
    return 'retaincase' in thiscommdct