def dependsOn(itemType, itemCustomizer=None, doc='', indexed=True,
    whenDeleted=reference.NULLIFY):
    frame = sys._getframe(1)
    locals = frame.f_locals
    if locals is frame.f_globals or '__module__' not in locals:
        raise TypeError('dependsOn can be used only from a class definition.')
    ref = reference(reftype=itemType, doc=doc, indexed=indexed, allowNone=
        True, whenDeleted=whenDeleted)
    if '__dependsOn_advice_data__' not in locals:
        addClassAdvisor(_dependsOn_advice)
    locals.setdefault('__dependsOn_advice_data__', []).append((itemType,
        itemCustomizer, ref))
    return ref