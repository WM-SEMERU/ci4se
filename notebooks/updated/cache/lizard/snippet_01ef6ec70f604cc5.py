def _WsdlHasMethod(self, method_name):
    return method_name in self.suds_client.wsdl.services[0].ports[0].methods