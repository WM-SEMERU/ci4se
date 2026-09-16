def check_effective(func):

    def wrapper(*args, **kwargs):
        if 'assessment_section_id' in kwargs or args and 'Section' in args[1
            ].get_identifier_namespace():
            try:
                assessment_section_id = kwargs['assessment_section_id']
            except KeyError:
                assessment_section_id = args[1]
            if not args[0].has_assessment_section_begun(assessment_section_id
                ) or args[0].is_assessment_section_over(assessment_section_id):
                raise IllegalState()
        else:
            if 'assessment_taken_id' in kwargs:
                assessment_taken_id = kwargs['assessment_taken_id']
            else:
                assessment_taken_id = args[1]
            assessment_taken = args[0]._get_assessment_taken(
                assessment_taken_id)
            if not assessment_taken.has_started(
                ) or assessment_taken.has_ended():
                raise IllegalState()
        return func(*args, **kwargs)
    return wrapper