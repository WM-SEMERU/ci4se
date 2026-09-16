def create_streaming_endpoint(access_token, name, description=
    'New Streaming Endpoint', scale_units='1'):
    path = '/StreamingEndpoints'
    endpoint = ''.join([ams_rest_endpoint, path])
    body = ('{ \t\t"Id":null, \t\t"Name":"' + name +
        '", \t\t"Description":"' + description +
        '", \t\t"Created":"0001-01-01T00:00:00", \t\t"LastModified":"0001-01-01T00:00:00", \t\t"State":null, \t\t"HostName":null, \t\t"ScaleUnits":"'
         + scale_units +
        '", \t\t"CrossSiteAccessPolicies":{ \t\t\t"ClientAccessPolicy":"<access-policy><cross-domain-access><policy><allow-from http-request-headers=\\"*\\"><domain uri=\\"http://*\\" /></allow-from><grant-to><resource path=\\"/\\" include-subpaths=\\"false\\" /></grant-to></policy></cross-domain-access></access-policy>", \t\t\t"CrossDomainPolicy":"<?xml version=\\"1.0\\"?><!DOCTYPE cross-domain-policy SYSTEM \\"http://www.macromedia.com/xml/dtds/cross-domain-policy.dtd\\"><cross-domain-policy><allow-access-from domain=\\"*\\" /></cross-domain-policy>" \t\t} \t}'
        )
    return do_ams_post(endpoint, path, body, access_token)