def get_feedback_from_submission(self, submission, only_feedback=False,
    show_everything=False, translation=gettext.NullTranslations()):
    if only_feedback:
        submission = {'text': submission.get('text', None), 'problems':
            dict(submission.get('problems', {}))}
    if 'text' in submission:
        submission['text'] = ParsableText(submission['text'], submission[
            'response_type'], show_everything, translation).parse()
    if 'problems' in submission:
        for problem in submission['problems']:
            if isinstance(submission['problems'][problem], str):
                submission['problems'][problem] = submission.get('result',
                    'crash'), ParsableText(submission['problems'][problem],
                    submission['response_type'], show_everything, translation
                    ).parse()
            else:
                submission['problems'][problem] = submission['problems'][
                    problem][0], ParsableText(submission['problems'][
                    problem][1], submission['response_type'],
                    show_everything, translation).parse()
    return submission