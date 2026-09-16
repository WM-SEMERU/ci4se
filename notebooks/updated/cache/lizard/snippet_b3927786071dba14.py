def _options_method_response_for_cors(self, allowed_origins,
    allowed_headers=None, allowed_methods=None, max_age=None,
    allow_credentials=None):
    ALLOW_ORIGIN = 'Access-Control-Allow-Origin'
    ALLOW_HEADERS = 'Access-Control-Allow-Headers'
    ALLOW_METHODS = 'Access-Control-Allow-Methods'
    MAX_AGE = 'Access-Control-Max-Age'
    ALLOW_CREDENTIALS = 'Access-Control-Allow-Credentials'
    HEADER_RESPONSE = lambda x: 'method.response.header.' + x
    response_parameters = {HEADER_RESPONSE(ALLOW_ORIGIN): allowed_origins}
    response_headers = {ALLOW_ORIGIN: {'type': 'string'}}
    if allowed_headers:
        response_parameters[HEADER_RESPONSE(ALLOW_HEADERS)] = allowed_headers
        response_headers[ALLOW_HEADERS] = {'type': 'string'}
    if allowed_methods:
        response_parameters[HEADER_RESPONSE(ALLOW_METHODS)] = allowed_methods
        response_headers[ALLOW_METHODS] = {'type': 'string'}
    if max_age is not None:
        response_parameters[HEADER_RESPONSE(MAX_AGE)] = max_age
        response_headers[MAX_AGE] = {'type': 'integer'}
    if allow_credentials is True:
        response_parameters[HEADER_RESPONSE(ALLOW_CREDENTIALS)] = "'true'"
        response_headers[ALLOW_CREDENTIALS] = {'type': 'string'}
    return {'summary': 'CORS support', 'consumes': ['application/json'],
        'produces': ['application/json'], self._X_APIGW_INTEGRATION: {
        'type': 'mock', 'requestTemplates': {'application/json':
        """{
  "statusCode" : 200
}
"""}, 'responses': {'default': {
        'statusCode': '200', 'responseParameters': response_parameters,
        'responseTemplates': {'application/json': '{}\n'}}}}, 'responses':
        {'200': {'description': 'Default response for CORS method',
        'headers': response_headers}}}