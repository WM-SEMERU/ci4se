def Copy(From, To):
    from benchbuild.utils.cmd import cp
    cp('-ar', '--reflink=auto', From, To)