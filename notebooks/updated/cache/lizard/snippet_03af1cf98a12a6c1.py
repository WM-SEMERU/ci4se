def params(self_, parameter_name=None):
    if self_.self is not None and self_.self._instance__params:
        self_.warning(
            'The Parameterized instance has instance parameters created using new-style param APIs, which are incompatible with .params. Use the new more explicit APIs on the .param accessor to query parameter instances.To query all parameter instances use .param.objects with the option to return either class or instance parameter objects. Alternatively use .param[name] indexing to access a specific parameter object by name.'
            )
    pdict = self_.objects(instance='existing')
    if parameter_name is None:
        return pdict
    else:
        return pdict[parameter_name]