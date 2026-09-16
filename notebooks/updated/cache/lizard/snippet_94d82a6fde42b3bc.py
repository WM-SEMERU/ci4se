def loading_failed(self, rdf_format_opts, uri=''):
    if uri:
        uri = ' <%s>' % str(uri)
    printDebug(
        '----------\nFatal error parsing graph%s\n(using RDF serializations: %s)'
         % (uri, str(rdf_format_opts)), 'red')
    printDebug(
        """----------
TIP: You can try one of the following RDF validation services
<http://mowl-power.cs.man.ac.uk:8080/validator/validate>
<http://www.ivan-herman.net/Misc/2008/owlrl/>"""
        )
    return