def mypy():
    if sys.version_info < (3, 4):
        print("Mypy doesn't work on python < 3.4")
        return
    if IS_TRAVIS:
        command = '{0} -m mypy {1} --ignore-missing-imports --strict'.format(
            PYTHON, PROJECT_NAME).strip()
    else:
        command = '{0} mypy {1} --ignore-missing-imports --strict'.format(
            PIPENV, PROJECT_NAME).strip()
    bash_process = subprocess.Popen(command.split(' '), stdout=subprocess.
        PIPE, stderr=subprocess.PIPE)
    out, err = bash_process.communicate()
    mypy_file = 'mypy_errors.txt'
    with open(mypy_file, 'w+') as lint_file:
        lines = out.decode().split('\n')
        for line in lines:
            if 'build_utils.py' in line:
                continue
            if 'test.py' in line:
                continue
            if 'tests.py' in line:
                continue
            if '/test_' in line:
                continue
            if '/tests_' in line:
                continue
            else:
                lint_file.writelines([line + '\n'])
    num_lines = sum(1 for line in open(mypy_file) if line and line.strip(' \n')
        )
    max_lines = 25
    if num_lines > max_lines:
        raise TypeError('Too many lines of mypy : {0}, max {1}'.format(
            num_lines, max_lines))