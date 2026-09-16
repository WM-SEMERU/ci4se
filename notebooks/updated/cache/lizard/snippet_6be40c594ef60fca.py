def main():
    args = get_args()
    tr = TestRail(project_dict[args.project])
    project = tr.project(project_dict[args.project])
    new_run = tr.run()
    new_run.name = 'Creating a new Run through the API'
    new_run.project = project
    new_run.include_all = True
    run = tr.add(new_run)
    print('Created new run: {0}'.format(run.name))
    PASSED = tr.status('passed')
    FAILED = tr.status('failed')
    BLOCKED = tr.status('blocked')
    tests = list(tr.tests(run))
    print('Found {0} tests'.format(len(tests)))
    for test_num, test in enumerate(tests):
        print('Executing test #{0}'.format(test_num))
        test_status = random.choice([PASSED, FAILED, BLOCKED])
        print('Updating test  #{0} with a status of {1}'.format(test_num,
            test_status.name))
        result = tr.result()
        result.test = test
        result.status = test_status
        result.comment = 'The test case was udpated via a script'
        tr.add(result)
    print('Finished, closing the run')
    tr.close(run)