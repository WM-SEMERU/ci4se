def _parseupload(self, node):
    if not isinstance(node, ElementTree._Element):
        try:
            node = clam.common.data.parsexmlstring(node)
        except:
            raise Exception(node)
    if node.tag != 'clamupload':
        raise Exception('Not a valid CLAM upload response')
    for node2 in node:
        if node2.tag == 'upload':
            for subnode in node2:
                if subnode.tag == 'error':
                    raise clam.common.data.UploadError(subnode.text)
                if subnode.tag == 'parameters':
                    if 'errors' in subnode.attrib and subnode.attrib['errors'
                        ] == 'yes':
                        errormsg = (
                            'The submitted metadata did not validate properly')
                        for parameternode in subnode:
                            if 'error' in parameternode.attrib:
                                errormsg = parameternode.attrib['error']
                                raise clam.common.data.ParameterError(
                                    errormsg + ' (parameter=' +
                                    parameternode.attrib['id'] + ')')
                        raise clam.common.data.ParameterError(errormsg)
    return True