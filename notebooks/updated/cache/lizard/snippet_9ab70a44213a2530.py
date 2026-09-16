def list(self):
    self._initialize_list()
    interested = True
    response = self._cloudFormation.list_stacks()
    print('Stack(s):')
    while interested:
        if 'StackSummaries' in response:
            for stack in response['StackSummaries']:
                stack_status = stack['StackStatus']
                if stack_status != 'DELETE_COMPLETE':
                    print('    [{}] - {}'.format(stack['StackStatus'],
                        stack['StackName']))
        next_token = response.get('NextToken', None)
        if next_token:
            response = self._cloudFormation.list_stacks(NextToken=next_token)
        else:
            interested = False
    return True