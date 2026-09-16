def GetSoapXMLForComplexType(self, type_name, value):
    schema = self.suds_client.wsdl.schema
    definition_type = schema.elements[type_name, self._namespace_override]
    marshaller = suds.mx.literal.Literal(schema)
    content = suds.mx.Content(tag=type_name, value=value, name=type_name,
        type=definition_type)
    data = marshaller.process(content)
    return data