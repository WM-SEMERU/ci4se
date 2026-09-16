def getPortType(self):
    wsdl = self.getService().getWSDL()
    binding = wsdl.bindings[self.binding]
    return wsdl.portTypes[binding.type]