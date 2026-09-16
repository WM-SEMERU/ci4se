def _getSmartIndenter(indenterName, qpart, indenter):
    indenterName = indenterName.lower()
    if indenterName in ('haskell', 'lilypond'):
        logger.warning(
            'Smart indentation for %s not supported yet. But you could be a hero who implemented it'
             % indenterName)
        from qutepart.indenter.base import IndentAlgNormal as indenterClass
    elif 'none' == indenterName:
        from qutepart.indenter.base import IndentAlgBase as indenterClass
    elif 'normal' == indenterName:
        from qutepart.indenter.base import IndentAlgNormal as indenterClass
    elif 'cstyle' == indenterName:
        from qutepart.indenter.cstyle import IndentAlgCStyle as indenterClass
    elif 'python' == indenterName:
        from qutepart.indenter.python import IndentAlgPython as indenterClass
    elif 'ruby' == indenterName:
        from qutepart.indenter.ruby import IndentAlgRuby as indenterClass
    elif 'xml' == indenterName:
        from qutepart.indenter.xmlindent import IndentAlgXml as indenterClass
    elif 'haskell' == indenterName:
        from qutepart.indenter.haskell import IndenterHaskell as indenterClass
    elif 'lilypond' == indenterName:
        from qutepart.indenter.lilypond import IndenterLilypond as indenterClass
    elif 'lisp' == indenterName:
        from qutepart.indenter.lisp import IndentAlgLisp as indenterClass
    elif 'scheme' == indenterName:
        from qutepart.indenter.scheme import IndentAlgScheme as indenterClass
    else:
        raise KeyError('Indenter %s not found' % indenterName)
    return indenterClass(qpart, indenter)