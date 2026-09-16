def include_sqlalchemy_models(nc, Base):
    from sqlalchemy.ext.declarative.clsregistry import _ModuleMarker
    for name, klass in Base._decl_class_registry.items():
        print(name, klass)
        if isinstance(klass, _ModuleMarker):
            continue
        add_script(nc, get_import_statement(klass))
        add_greeting(nc, '* **{}** - {}'.format(klass.__name__,
            get_dotted_path(klass)))