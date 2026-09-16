def filter_all_contents(value: ecore.EPackage, type_):
    return (c for c in value.eAllContents() if isinstance(c, type_))