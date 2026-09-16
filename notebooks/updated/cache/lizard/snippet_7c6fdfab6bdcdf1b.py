def _get_deployment_instance_diagnostics(awsclient, deployment_id, instance_id
    ):
    client_codedeploy = awsclient.get_client('codedeploy')
    request = {'deploymentId': deployment_id, 'instanceId': instance_id}
    response = client_codedeploy.get_deployment_instance(**request)
    for i, event in enumerate(response['instanceSummary']['lifecycleEvents']):
        if event['status'] == 'Failed':
            return event['diagnostics']['errorCode'], event['diagnostics'][
                'scriptName'], event['diagnostics']['message'], event[
                'diagnostics']['logTail']
    return None