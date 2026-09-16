def _GenerateSection(self, problem_type):
    if problem_type == transitfeed.TYPE_WARNING:
        dataset_problems = self._dataset_warnings
        heading = 'Warnings'
    else:
        dataset_problems = self._dataset_errors
        heading = 'Errors'
    if not dataset_problems:
        return ''
    prefix = '<h2 class="issueHeader">%s:</h2>' % heading
    dataset_sections = []
    for dataset_merger, problems in dataset_problems.items():
        dataset_sections.append('<h3>%s</h3><ol>%s</ol>' % (dataset_merger.
            FILE_NAME, '\n'.join(problems)))
    body = '\n'.join(dataset_sections)
    return prefix + body