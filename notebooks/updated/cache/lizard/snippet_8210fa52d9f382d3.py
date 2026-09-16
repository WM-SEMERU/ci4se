def run(configobj=None, editpars=False):
    if configobj is None:
        configobj = teal.teal(__taskname__, loadOnly=not editpars)
    update(configobj['input'], configobj['refdir'], local=configobj['local'
        ], interactive=configobj['interactive'], wcsupdate=configobj[
        'wcsupdate'])