def ugettext(self, text):
    runtime_service = self.runtime.service(self, 'i18n')
    runtime_ugettext = runtime_service.ugettext
    return runtime_ugettext(text)