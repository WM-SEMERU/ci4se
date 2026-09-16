def report(self):
    print('\n{}{}{}'.format(c.Style.BRIGHT, c.Fore.CYAN, 'Report:'))
    print('{!s:<85}{!s:<20}'.format('', 'Validations'))
    print('{!s:<60}{!s:<25}{!s:<10}{!s:<10}'.format('Profile:',
        'Execution:', 'Passed:', 'Failed:'))
    for r in self.reports:
        d = r.data
        if not d.get('selected'):
            continue
        execution_color = c.Fore.RED
        execution_text = 'Failed'
        if d.get('execution_success'):
            execution_color = c.Fore.GREEN
            execution_text = 'Passed'
        pass_count_color = c.Fore.GREEN
        pass_count = d.get('validation_pass_count', 0)
        fail_count = d.get('validation_fail_count', 0)
        fail_count_color = c.Fore.GREEN
        if fail_count > 0:
            fail_count_color = c.Fore.RED
        print('{!s:<60}{}{!s:<25}{}{!s:<10}{}{!s:<10}'.format(d.get('name'),
            execution_color, execution_text, pass_count_color, pass_count,
            fail_count_color, fail_count))
    if self.args.report:
        with open(self.args.report, 'w') as outfile:
            outfile.write(str(self.reports))