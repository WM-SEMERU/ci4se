def AddTemplate(self, template, parameters):
    try:
        module = load_module(template)
    except ImportError as e:
        raise dbus.exceptions.DBusException('Cannot add template %s: %s' %
            (template, str(e)), name='org.freedesktop.DBus.Mock.TemplateError')
    if hasattr(module, 'IS_OBJECT_MANAGER') and module.IS_OBJECT_MANAGER:
        self._set_up_object_manager()
    for symbol in dir(module):
        fn = getattr(module, symbol)
        if '_dbus_interface' in dir(fn) and ('_dbus_is_signal' not in dir(
            fn) or not fn._dbus_is_signal):
            setattr(self.__class__, symbol, fn)
            self.methods.setdefault(fn._dbus_interface, {})[str(symbol)
                ] = fn._dbus_in_signature, fn._dbus_out_signature, '', fn
    if parameters is None:
        parameters = {}
    module.load(self, parameters)
    self._template = template
    self._template_parameters = parameters