def has_previous_assessment_section(self, assessment_section_id):
    try:
        self.get_previous_assessment_section(assessment_section_id)
    except errors.IllegalState:
        return False
    else:
        return True