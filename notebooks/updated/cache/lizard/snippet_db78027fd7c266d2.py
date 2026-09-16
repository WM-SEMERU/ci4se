def pelix_infos(self):
    framework = self.__context.get_framework()
    return {'version': framework.get_version(), 'properties': framework.
        get_properties()}