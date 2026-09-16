def solution(self):
    num = self.num
    solution_file = os.path.join(EULER_DATA, 'solutions.txt')
    solution_line = linecache.getline(solution_file, num)
    try:
        answer = solution_line.split('. ')[1].strip()
    except IndexError:
        answer = None
    if answer:
        return answer
    else:
        msg = 'Answer for problem %i not found in solutions.txt.' % num
        click.secho(msg, fg='red')
        click.echo(
            'If you have an answer, consider submitting a pull request to EulerPy on GitHub.'
            )
        sys.exit(1)