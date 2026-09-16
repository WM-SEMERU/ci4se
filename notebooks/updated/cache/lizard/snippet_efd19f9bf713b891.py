def delete_api(self, ret):
    exists_response = __salt__['boto_apigateway.api_exists'](name=self.
        rest_api_name, description=_Swagger.AWS_API_DESCRIPTION, **self.
        _common_aws_args)
    if exists_response.get('exists'):
        if __opts__['test']:
            ret['comment'] = 'Rest API named {0} is set to be deleted.'.format(
                self.rest_api_name)
            ret['result'] = None
            ret['abort'] = True
            return ret
        delete_api_response = __salt__['boto_apigateway.delete_api'](name=
            self.rest_api_name, description=_Swagger.AWS_API_DESCRIPTION,
            **self._common_aws_args)
        if not delete_api_response.get('deleted'):
            ret['result'] = False
            ret['abort'] = True
            if 'error' in delete_api_response:
                ret['comment'] = 'Failed to delete rest api: {0}.'.format(
                    delete_api_response['error']['message'])
            return ret
        ret = _log_changes(ret, 'delete_api', delete_api_response)
    else:
        ret['comment'
            ] = 'api already absent for swagger file: {0}, desc: {1}'.format(
            self.rest_api_name, self.info_json)
    return ret