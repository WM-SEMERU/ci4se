def xpath(self, xpath_str):
    return super(BaseOxmlElement, self).xpath(xpath_str, namespaces=_nsmap)