def health(self, request, project):
    revision = request.query_params.get('revision')
    try:
        push = Push.objects.get(revision=revision, repository__name=project)
    except Push.DoesNotExist:
        return Response('No push with revision: {0}'.format(revision),
            status=HTTP_404_NOT_FOUND)
    push_health_test_failures = get_push_health_test_failures(push,
        REPO_GROUPS['trunk'])
    test_result = 'fail' if len(push_health_test_failures['needInvestigation']
        ) else 'pass'
    return Response({'revision': revision, 'id': push.id, 'result':
        test_result, 'metrics': [{'name': 'Tests', 'result': test_result,
        'failures': push_health_test_failures}, {'name':
        'Builds (Not yet implemented)', 'result': 'pass', 'details': [
        'Wow, everything passed!']}, {'name':
        'Linting (Not yet implemented)', 'result': 'pass', 'details': [
        'Gosh, this code is really nicely formatted.']}, {'name':
        'Coverage (Not yet implemented)', 'result': 'pass', 'details': [
        'Covered 42% of the tests that are needed for feature ``foo``.',
        'Covered 100% of the tests that are needed for feature ``bar``.',
        'The ratio of people to cake is too many...']}, {'name':
        'Performance (Not yet implemented)', 'result': 'pass', 'details': [
        'Ludicrous Speed']}]})